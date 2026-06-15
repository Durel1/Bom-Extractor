from bom_extractor.infrastructure.parsers.csv_parser import CsvBomParser


class ParserFactory:

    @staticmethod
    def create(file_type: str):

        parsers = {
            "csv": CsvBomParser
        }

        parser_class = parsers.get(file_type)

        if parser_class is None:
            raise ValueError(
                f"Unsupported file type: {file_type}"
            )

        return parser_class()