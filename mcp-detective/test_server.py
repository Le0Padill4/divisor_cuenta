import pytest

import server


@pytest.fixture(autouse=True)
def alertas_aisladas(monkeypatch):
    monkeypatch.setattr(server, "ALERTAS", {})


def test_lista_los_tres_casos_con_sus_cantidades():
    assert [(c["caso_id"], c["cantidad_eventos"]) for c in server.listar_casos()] == [
        ("INC-001", 2), ("INC-002", 6), ("INC-003", 5),
    ]


def test_consulta_los_seis_fallos_de_admin():
    eventos = server.consultar_eventos("INC-002")
    assert len(eventos) == 6
    assert all(e["usuario"] == "admin" and e["evento"] == "LOGIN_FAILED" for e in eventos)


def test_consulta_de_caso_inexistente():
    with pytest.raises(ValueError, match="El caso INC-999 no existe"):
        server.consultar_eventos("INC-999")


def test_registra_alerta_valida():
    alerta = server.registrar_alerta("INC-003", "alto", "  Requiere revisión  ")
    assert alerta == {
        "caso_id": "INC-003", "nivel": "alto",
        "motivo": "Requiere revisión", "estado": "registrada",
    }
    assert server.ALERTAS["INC-003"] == alerta


def test_rechaza_duplicado_y_conserva_la_primera_alerta():
    primera = server.registrar_alerta("INC-003", "alto", "Requiere revisión")
    with pytest.raises(ValueError, match="Alerta duplicada"):
        server.registrar_alerta("INC-003", "bajo", "Otro motivo")
    assert server.ALERTAS == {"INC-003": primera}


@pytest.mark.parametrize(("caso", "nivel", "motivo", "error"), [
    ("INC-999", "alto", "Revisar", "no existe"),
    ("INC-002", "critico", "Intentos repetidos", "Nivel inválido"),
    ("INC-002", "medio", "   ", "motivo no puede estar vacío"),
    ("INC-002", "medio", "", "motivo no puede estar vacío"),
])
def test_rechaza_parametros_invalidos_sin_guardar(caso, nivel, motivo, error):
    with pytest.raises(ValueError, match=error):
        server.registrar_alerta(caso, nivel, motivo)
    assert server.ALERTAS == {}
