import pytest
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def mongo_client():
    uri = os.getenv("MONGO_URI")
    client = MongoClient(uri)
    yield client #o yield ele serve para oque esta abaixo dele vai se encerrar e vai ser limpado a configuração conexão e oque estiver acima são as configurações que usamos nos testes
    client.close()


@pytest.fixture(scope="function")
def test_db(mongo_client):
    db = mongo_client["burguer_app_test"]    #inseire o banco de dados na função do mongo_client

    db["users"].delete_many({}) #serve para limpar o banco de dados na coluna "users"
    db["pedidos"].delete_many({}) #serve para limpar o banco de dados na coluna "pedidos"

    yield db