from abc import ABC, abstractmethod
from src.model.entities.eventos_link import EventosLink


class EventosRepositoryInterface(ABC):
    @abstractmethod
    def insert_event(self, event_id: str, subscrober_id: int) -> None:
        pass

    @abstractmethod
    def select_event(self, event_id: str, subscrober_id: int) -> EventosLink:
        pass
