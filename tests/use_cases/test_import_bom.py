from bom_extractor.application.use_cases.import_bom import ImportBomUseCase
from bom_extractor.parser import BomCsvParser
from bom_extractor.validator import BomValidator
from bom_extractor.infrastructure.persistence.database import create_session_factory
from bom_extractor.infrastructure.persistence.sql_repository import SqlBomRepository


def test_import_bom_use_case_imports_csv_into_database():
    Session = create_session_factory("sqlite:///:memory:")
    session = Session()

    parser = BomCsvParser()
    validator = BomValidator()
    repository = SqlBomRepository(session)

    use_case = ImportBomUseCase(parser, validator, repository)

    use_case.execute("data/sample_bom.csv")

    saved_parts = repository.find_all()

    assert len(saved_parts) == 6
    assert saved_parts[0].part_id == "P001"