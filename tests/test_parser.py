from bom_extractor.infrastructure.parsers.parser import BomCsvParser


def test_parse_returns_parts():
    parser = BomCsvParser()

    parts = parser.parse("data/sample_bom.csv")

    assert len(parts) == 6


def test_first_part_is_root():
    parser = BomCsvParser()

    parts = parser.parse("data/sample_bom.csv")

    root = parts[0]

    assert root.part_id == "P001"
    assert root.name == "Vélo"
    assert root.parent_id is None