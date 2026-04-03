import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))# quer dizer que vai subir o path da pasta teste -> auth-service -> burguer app, podendo acessar order-service ou product-service ou user-service, por isso tem 2 os.path.dirname para subir path, os.path.abspath vai pegar o caminho do arquivo, os os dirname vai subir pasta e vai adicionaro a lista do interpretador o caminho de burguer-app
from models.user_model import serialize_user

def test_serialize_user_complet():#comeco da funcão tem que começar com test
    user: dict[str] = {
        "email": "teste@exemplo.com",
        "name": "Teste Usuário",
        "address": "98 rua exemplo",
        "role": "admin"
    }

    resultado = serialize_user(user)

    esperado: dict[str] = {
        "email": "teste@exemplo.com",
        "name": "Teste Usuário",
        "address": "98 rua exemplo",
        "role": "admin"
    }


    assert resultado == esperado#o assert serve para testar se a condição do teste para ser validado para saber se o comportamente e o esperado, usamos o assert se não der erro, o teste funcionou e retornou o valor esperado senão deu erro e o valor nao veio como foi esperado



def test_serialize_user_incomplet():#comeco da funcão tem que começar com test
    user: dict[str] = {
        "email": "teste@exemplo.com",
    }

    resultado = serialize_user(user)

    esperado: dict[str] = {#no caso aqui como so um campo foi colocado oque deve ser testado ou colocado, oque foi definido na função original
        "email": "teste@exemplo.com",
        "name": "",
        "address": "",
        "role": "cliente"
    }


    assert resultado == esperado#o assert serve para testar se a condição do teste para ser validado para saber se o comportamente e o esperado, usamos o assert se não der erro, o teste funcionou e retornou o valor esperado senão deu erro e o valor nao veio como foi esperado    

def test_serialize_user_none():#comeco da funcão tem que começar com test
    user: dict[str] = {
    }

    resultado = serialize_user(user)

    esperado: dict[str] = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente"
    }


    assert resultado == esperado#o assert serve para testar se a condição do teste para ser validado para saber se o comportamente e o esperado, usamos o assert se não der erro, o teste funcionou e retornou o valor esperado senão deu erro e o valor nao veio como foi esperado


def test_serialize_user_int():#comeco da funcão tem que começar com test
    with pytest.raises(AttributeError):#with e para executar algo e quando terminar de executar fecha e limpa da memoria, pytest.raises(AttributeError) e ele tambem faz uma outra condição que funciona com um assert o with que faz a verificação como se fosse um assert o assert essta implicito no with, quer dizer que ele vai testar se vai dar o erro AttributeError se der que dizer que ele passo no teste, pois o serilize_user() espera um dicionario, então se passar o teste quer dizer que o codigo não consegue receber um valor inteiro
        serialize_user(12345)



def test_serialize_user_string():#comeco da funcão tem que começar com test
    with pytest.raises(AttributeError):#with e para executar algo e quando terminar de executar fecha e limpa da memoria, pytest.raises(AttributeError) e ele tambem faz uma outra condição que funciona com um assert o with que faz a verificação como se fosse um assert o assert essta implicito no with, quer dizer que ele vai testar se vai dar o erro AttributeError se der que dizer que ele passo no teste, pois o serilize_user() espera um dicionario, então se passar o teste quer dizer que o codigo não consegue receber um valor string
        serialize_user("testando") 



def test_serialize_user_Inexperado():#comeco da funcão tem que começar com test
    user: dict[str] = {
        "email": 12345490,
        "name": ["teste1", ["teste2"]],
        "address": True,
        "role": 29.0
    }

    resultado = serialize_user(user)

    esperado: dict[str] = {
        "email": 12345490,
        "name": ["teste1", ["teste2"]],
        "address": True,
        "role": 29.0
    }



    assert resultado == esperado#o assert serve para testar se a condição do teste para ser validado para saber se o comportamente e o esperado, usamos o assert se não der erro, o teste funcionou e retornou o valor esperado senão deu erro e o valor nao veio como foi esperado


def test_serialize_user_Inexperado():#comeco da funcão tem que começar com test
    user: dict[str] = {
        "email": None,
        "name": None,
        "address": None,
        "role": None
    }

    resultado = serialize_user(user)

    esperado: dict[str] = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente"
    }
    #obs: aqui no caso não vai pasar o teste porque a funcão originial ele quer receber no dicionario valores realemente


    assert resultado == esperado#o assert serve para testar se a condição do teste para ser validado para saber se o comportamente e o esperado, usamos o assert se não der erro, o teste funcionou e retornou o valor esperado senão deu erro e o valor nao veio como foi esperado


""" 
    obs:
    1. usando no cmd ou powershell pytest -v vai mostrar melhor oque foi testado e oque passou ou não
    2. se tiver mais de um arquivo de teste pode especificar qual arquivo e para usar: pytest ./test/test_model_user.py, que ira rodar o arquivo
"""