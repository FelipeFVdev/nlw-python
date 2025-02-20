import pytest
from src.model.repositories.subscribers_repository import SubscribersRepository


@pytest.mark.skip("Insert in DB")
def test_insert_subscriber():
    subscriber_info = {
        "nome": "meuNome",
        "email": "meuEmail@gmail.com",
        "evento_id": 1,
    }
    sub_repo = SubscribersRepository()
    sub_repo.insert_subscriber(subscriber_info)


@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "meuEmail@gmail.com"
    evento_id = 1

    sub_repo = SubscribersRepository()
    data = sub_repo.select_subscriber(email, evento_id)
    print(data.nome)
