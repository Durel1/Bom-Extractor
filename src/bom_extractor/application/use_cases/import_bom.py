from bom_extractor.validator import BomValidator


class ImportBomUseCase:
    def __init__(self, parser, validator: BomValidator, repository):
        self.parser = parser
        self.validator = validator
        self.repository = repository

    def execute(self, file_path: str) -> None:
        parts = self.parser.parse(file_path)
        self.validator.validate(parts)
        self.repository.save_all(parts)