"""Herramientas MCP para investigar los casos simulados de Centinela."""

import json
from pathlib import Path

from mcp.server import MCPServer

mcp = MCPServer("MCP Detective")
CASOS = json.loads(Path(__file__).with_name("casos.json").read_text(encoding="utf-8"))
ALERTAS: dict[str, dict[str, str]] = {}


def _obtener_caso(caso_id: str) -> dict:
    if caso_id not in CASOS:
        raise ValueError(f"El caso {caso_id} no existe.")
    return CASOS[caso_id]


@mcp.tool()
def listar_casos() -> list[dict]:
    """Lista el identificador, el sistema y la cantidad de eventos de cada caso."""
    return [
        {"caso_id": caso_id, "sistema": caso["sistema"], "cantidad_eventos": len(caso["eventos"])}
        for caso_id, caso in CASOS.items()
    ]


@mcp.tool()
def consultar_eventos(caso_id: str) -> list[dict]:
    """Devuelve los eventos del caso indicado o informa que el caso no existe."""
    return _obtener_caso(caso_id)["eventos"]


@mcp.tool()
def registrar_alerta(caso_id: str, nivel: str, motivo: str) -> dict:
    """Registra una alerta en memoria por caso, con nivel bajo, medio o alto y un motivo."""
    _obtener_caso(caso_id)
    if nivel not in ("bajo", "medio", "alto"):
        raise ValueError("Nivel inválido: usa bajo, medio o alto.")
    if not isinstance(motivo, str) or not motivo.strip():
        raise ValueError("El motivo no puede estar vacío.")
    if caso_id in ALERTAS:
        raise ValueError(f"Alerta duplicada: {caso_id} ya tiene una alerta registrada.")

    alerta = {"caso_id": caso_id, "nivel": nivel, "motivo": motivo.strip(), "estado": "registrada"}
    ALERTAS[caso_id] = alerta
    return alerta


if __name__ == "__main__":
    mcp.run(transport="stdio")
