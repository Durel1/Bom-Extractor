from abc import ABC, abstractmethod

from bom_extractor.models import Part


class BomRepository(ABC):

    @abstractmethod
    def save_all(self, parts: list[Part]) -> None:
        pass

    @abstractmethod
    def find_all(self) -> list[Part]:
        pass