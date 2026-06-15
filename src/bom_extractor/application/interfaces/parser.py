from abc import ABC, abstractmethod

from bom_extractor.models import Part


class BomParser(ABC):

    @abstractmethod
    def parse(
        self,
        file_path: str
    ) -> list[Part]:
        pass