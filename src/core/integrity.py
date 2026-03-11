"""Modulo de integridade de arquivos via SHA-256.

Garante rastreabilidade e prova de que arquivos nao foram alterados.
Usado em audit logs e verificacao de dados de entrada/saida.
"""

import hashlib
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

BUFFER_SIZE = 65536  # 64KB chunks para arquivos grandes


def calcular_sha256(file_path: str | Path) -> str:
    """Calcula hash SHA-256 de um arquivo.

    Args:
        file_path: Caminho do arquivo.

    Returns:
        String hexadecimal do hash SHA-256.

    Raises:
        FileNotFoundError: Se o arquivo nao existe.
        PermissionError: Se nao tem permissao de leitura.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo nao encontrado: {file_path}")

    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            sha256.update(data)

    hash_hex = sha256.hexdigest()
    logger.debug("SHA-256 de %s: %s", file_path.name, hash_hex)
    return hash_hex


def verificar_integridade(file_path: str | Path, hash_esperado: str) -> bool:
    """Verifica se o hash de um arquivo confere com o esperado.

    Args:
        file_path: Caminho do arquivo.
        hash_esperado: Hash SHA-256 esperado (hex).

    Returns:
        True se os hashes conferem, False caso contrario.
    """
    hash_calculado = calcular_sha256(file_path)
    match = hash_calculado == hash_esperado.lower()

    if not match:
        logger.warning(
            "INTEGRIDADE FALHOU para %s: esperado=%s, calculado=%s",
            Path(file_path).name,
            hash_esperado[:16] + "...",
            hash_calculado[:16] + "...",
        )
    else:
        logger.debug("Integridade OK para %s", Path(file_path).name)

    return match


def calcular_sha256_texto(texto: str) -> str:
    """Calcula hash SHA-256 de uma string (para configs, regras, etc.).

    Args:
        texto: Texto a ser hasheado.

    Returns:
        String hexadecimal do hash SHA-256.
    """
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def info_arquivo(file_path: str | Path) -> dict:
    """Retorna metadados de um arquivo para audit log.

    Args:
        file_path: Caminho do arquivo.

    Returns:
        Dict com nome, tamanho_bytes e hash_sha256.
    """
    file_path = Path(file_path)
    return {
        "nome": file_path.name,
        "caminho": str(file_path),
        "tamanho_bytes": file_path.stat().st_size,
        "hash_sha256": calcular_sha256(file_path),
    }
