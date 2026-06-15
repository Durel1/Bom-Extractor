from bom_extractor.infrastructure.persistence.database import create_session_factory
from bom_extractor.infrastructure.persistence.sql_repository import SqlBomRepository
from bom_extractor.models import Part


def test_repository_saves_and_finds_parts():
    Session = create_session_factory("sqlite:///:memory:")
    session = Session()

    repository = SqlBomRepository(session)

    parts = [
        Part("P001", "Vélo", None, 1, 0.0, "ASSEMBLY"),
        Part("P002", "Roue avant", "P001", 1, 1.2, "Aluminium"),
    ]

    repository.save_all(parts)

    saved_parts = repository.find_all()

    assert len(saved_parts) == 2
    assert saved_parts[0].part_id == "P001"