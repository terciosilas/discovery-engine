"""Modulo de auditoria append-only.

Gera logs de execucao no formato JSON conforme GOVERNANCA.md.
Logs sao imutaveis (append-only) com retencao minima de 5 anos.
"""

import json
import logging
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.core.integrity import calcular_sha256, info_arquivo

logger = logging.getLogger(__name__)

# Diretorio padrao de audit logs
DEFAULT_AUDIT_DIR = Path(__file__).resolve().parent.parent.parent / "audit_logs"


class AuditLogger:
    """Logger de auditoria append-only para rastreabilidade completa.

    Cada execucao gera um registro JSON imutavel com:
    - ID unico (UUID v4)
    - Timestamps de inicio/fim
    - Hashes SHA-256 de inputs e outputs
    - Contagens de registros
    - Status e anomalias
    """

    def __init__(
        self,
        operador: str = "system",
        audit_dir: str | Path | None = None,
        modulo: str = "geral",
    ) -> None:
        """Inicializa o audit logger.

        Args:
            operador: Identificacao do usuario.
            audit_dir: Diretorio para salvar logs (padrao: audit_logs/).
            modulo: Nome do modulo/pipeline sendo executado.
        """
        self.audit_dir = Path(audit_dir) if audit_dir else DEFAULT_AUDIT_DIR
        self.audit_dir.mkdir(parents=True, exist_ok=True)

        self.execution_id = str(uuid.uuid4())
        self.operador = operador
        self.modulo = modulo
        self.timestamp_inicio = datetime.now(timezone.utc).isoformat()
        self.timestamp_fim: str | None = None

        self.arquivos_input: list[dict] = []
        self.arquivos_output: list[dict] = []
        self.registros_lidos: int = 0
        self.registros_validos: int = 0
        self.registros_processados: int = 0
        self.registros_rejeitados: int = 0
        self.anomalias: list[str] = []
        self.status: str = "EM_EXECUCAO"
        self.erro: str | None = None
        self.metadados: dict[str, Any] = {}

        logger.info(
            "[AUDIT] Execucao iniciada: %s | Modulo: %s | Operador: %s",
            self.execution_id[:8],
            self.modulo,
            self.operador,
        )

    def registrar_input(self, file_path: str | Path) -> None:
        """Registra um arquivo de entrada com hash SHA-256.

        Args:
            file_path: Caminho do arquivo de input.
        """
        info = info_arquivo(file_path)
        self.arquivos_input.append(info)
        logger.info("[AUDIT] Input registrado: %s (%d bytes)", info["nome"], info["tamanho_bytes"])

    def registrar_output(self, file_path: str | Path) -> None:
        """Registra um arquivo de saida com hash SHA-256.

        Args:
            file_path: Caminho do arquivo de output.
        """
        info = info_arquivo(file_path)
        self.arquivos_output.append(info)
        logger.info("[AUDIT] Output registrado: %s (%d bytes)", info["nome"], info["tamanho_bytes"])

    def registrar_contagens(
        self,
        lidos: int = 0,
        validos: int = 0,
        processados: int = 0,
        rejeitados: int = 0,
    ) -> None:
        """Atualiza contagens de registros.

        Args:
            lidos: Total de registros lidos.
            validos: Registros que passaram validacao.
            processados: Registros efetivamente processados.
            rejeitados: Registros rejeitados.
        """
        self.registros_lidos = lidos
        self.registros_validos = validos
        self.registros_processados = processados
        self.registros_rejeitados = rejeitados

    def registrar_anomalia(self, descricao: str) -> None:
        """Registra uma anomalia/warning.

        Args:
            descricao: Descricao da anomalia encontrada.
        """
        self.anomalias.append(descricao)
        logger.warning("[AUDIT] Anomalia: %s", descricao)

    def adicionar_metadado(self, chave: str, valor: Any) -> None:
        """Adiciona metadado customizado ao registro de auditoria.

        Args:
            chave: Nome do metadado.
            valor: Valor (deve ser serializavel em JSON).
        """
        self.metadados[chave] = valor

    def finalizar(self, status: str = "SUCESSO", erro: str | None = None) -> Path:
        """Finaliza a execucao e salva o log de auditoria.

        Args:
            status: SUCESSO | SUCESSO_COM_ALERTAS | FALHA
            erro: Mensagem de erro se status == FALHA.

        Returns:
            Path do arquivo de log gerado.
        """
        self.timestamp_fim = datetime.now(timezone.utc).isoformat()

        if self.anomalias and status == "SUCESSO":
            status = "SUCESSO_COM_ALERTAS"

        self.status = status
        self.erro = erro

        registro = self._montar_registro()

        # Salvar no subdiretorio correto
        subdir = self.audit_dir / "executions"
        subdir.mkdir(parents=True, exist_ok=True)

        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"exec_{self.modulo}_{timestamp_str}_{self.execution_id[:8]}.json"
        filepath = subdir / filename

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(registro, f, ensure_ascii=False, indent=2)

        logger.info(
            "[AUDIT] Execucao finalizada: %s | Status: %s | Registros: %d lidos, %d processados, %d rejeitados",
            self.execution_id[:8],
            self.status,
            self.registros_lidos,
            self.registros_processados,
            self.registros_rejeitados,
        )

        return filepath

    def _montar_registro(self) -> dict:
        """Monta o registro de auditoria completo."""
        registro = {
            "execution_id": self.execution_id,
            "modulo": self.modulo,
            "timestamp_inicio": self.timestamp_inicio,
            "timestamp_fim": self.timestamp_fim,
            "operador": self.operador,
            "versao_codigo": self._get_git_hash(),
            "arquivos_input": self.arquivos_input,
            "arquivos_output": self.arquivos_output,
            "registros_lidos": self.registros_lidos,
            "registros_validos": self.registros_validos,
            "registros_processados": self.registros_processados,
            "registros_rejeitados": self.registros_rejeitados,
            "anomalias": self.anomalias,
            "status": self.status,
            "erro": self.erro,
        }
        if self.metadados:
            registro["metadados"] = self.metadados
        return registro

    @staticmethod
    def _get_git_hash() -> str:
        """Tenta obter o hash do commit atual do git."""
        import subprocess

        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        return "sem-versionamento"
