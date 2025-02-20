from src.model.repositories.interfaces.subscribers_repository import (
    SubscribersRepositoryInterface,
)

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class SubscribersCreator:
    def __init__(self, sub_repo: SubscribersRepositoryInterface):
        self.__sub_repo = sub_repo

    def create_sub(self, http_request: HttpRequest) -> HttpResponse:
        subscriber_info = http_request.body["data"]
        subscriber_email = subscriber_info["email"]
        evento_id = subscriber_info["evento_id"]

        self.__check_sub(subscriber_email, evento_id)
        self.__insert_sub(subscriber_info)

        return self.__format_response(subscriber_info)

    def __check_sub(self, subscriber_email: str, evento_id: int) -> None:
        response = self.__sub_repo.select_subscriber(subscriber_email, evento_id)
        if response:
            raise Exception("Subscriber already exists!")

    def __insert_sub(self, subscriber_info: dict) -> None:
        self.__sub_repo.insert_subscriber(subscriber_info)

    def __format_response(self, subscriber_info: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": 1,
                    "Attributes": subscriber_info,
                }
            },
            status_code=201,
        )
