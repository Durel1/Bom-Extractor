from bom_extractor.application.interfaces.repository import BomRepository
from bom_extractor.infrastructure.persistence.entities import PartEntity
from bom_extractor.models import Part


class SqlBomRepository(BomRepository):
    def __init__(self, session):
        self.session = session

    def save_all(self, parts: list[Part]) -> None:
        for part in parts:
            entity = PartEntity(
                part_id=part.part_id,
                name=part.name,
                parent_id=part.parent_id,
                quantity=part.quantity,
                unit_weight=part.unit_weight,
                material=part.material,
            )

            self.session.merge(entity)

        self.session.commit()

    def find_all(self) -> list[Part]:
        entities = self.session.query(PartEntity).all()

        return [
            Part(
                part_id=entity.part_id,
                name=entity.name,
                parent_id=entity.parent_id,
                quantity=entity.quantity,
                unit_weight=entity.unit_weight,
                material=entity.material,
            )
            for entity in entities
        ]