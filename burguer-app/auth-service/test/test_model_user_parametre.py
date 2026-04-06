import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user_model import serialize_user

@pytest.mark.parametrize("user, esperado", [
    (
        {
            "email": "teste@exemplo.com",
            "name": "Teste Usuário",
            "address": "98 rua exemplo",
            "role": "admin"
        },
        {
            "email": "teste@exemplo.com",
            "name": "Teste Usuário",
            "address": "98 rua exemplo",
            "role": "admin"
        }
    ),
    (
        {
            "email": "teste@exemplo.com"
        },
        {
            "email": "teste@exemplo.com"
        }
    ),
    (
        { },
        {
            "email": None,
            "name": "",
            "address": "",
            "role": "cliente"
        }
    ),
    (
        {
            "email": 12345490,
            "name": ["teste1", ["teste2"]],
            "address": True,
            "role": 29.0
        },
        {
            "email": 12345490,
            "name": ["teste1", ["teste2"]],
            "address": True,
            "role": 29.0
        }
    )
])
def test_model_user_paratrize(user, esperado):
    resultado = serialize_user(user)
    assert user == esperado



@pytest.mark.parametrize("entrada",[
    None,
    "string",
    12345,
    []
])
def test_model_user_parametrize_valor_unico(entrada):
    with pytest.raises(AttributeError):
        serialize_user(entrada)