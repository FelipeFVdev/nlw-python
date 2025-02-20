from src.model.repositories.interfaces.eventos_repository import (
    EventosRepositoryInterface,
)

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse


class EventsCreator:
    def __init__(self, event_repo: EventosRepositoryInterface):
        self.__event_repo = event_repo

    def create_event(self, http_request: HttpRequest) -> HttpResponse:
        event_info = http_request.body["data"]
        event_name = event_info["name"]

        self.__check_event(event_name)
        self.__insert_event(event_name)

        return self.__format_response(event_name)

    def __check_event(self, event_name: str) -> None:
        response = self.__event_repo.select_event(event_name)
        if response:
            raise Exception("Event already exists!")

    def __insert_event(self, event_name: str) -> None:
        self.__event_repo.insert_event(event_name)

    def __format_response(self, event_name: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "Event",
                    "count": 1,
                    "Attributes": {
                        "event_name": event_name,
                    },
                }
            },
            status_code=201,
        )
