import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.user_model import serialize_user


@pytest.mark.usefixtures("test_db")
def test_user_db(test_db):
    user = {
        "email": "lucas@gmail.com",
        "name": "lucas gaia"
    }

    result = test_db["users"].insert_one(user)
    encontrado = test_db["users"].find_one({"_id": result.inserted_id})
    assert encontrado["email"] == user["email"]