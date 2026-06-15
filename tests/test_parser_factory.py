import pytest

from bom_extractor.application.factories.parser_factory import ParserFactory
from bom_extractor.infrastructure.parsers.csv_parser import CsvBomParser


def test_create_csv_parser():

    parser = ParserFactory.create("csv")

    assert isinstance(
        parser,
        CsvBomParser
    )


def test_unknown_parser_type():

    with pytest.raises(ValueError):
        ParserFactory.create("xml")