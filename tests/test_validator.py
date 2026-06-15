import pytest

from bom_extractor.models import Part
from bom_extractor.validator import BomValidator


def test_validator_accepts_valid_bom():
    parts = [
        Part("P001", "Vélo", None, 1, 0.0, "ASSEMBLY"),
        Part("P002", "Roue avant", "P001", 1, 1.2, "Aluminium"),
    ]

    validator = BomValidator()

    validator.validate(parts)


def test_validator_rejects_duplicate_part_ids():
    parts = [
        Part("P001", "Vélo", None, 1, 0.0, "ASSEMBLY"),
        Part("P001", "Roue avant", "P001", 1, 1.2, "Aluminium"),
    ]

    validator = BomValidator()

    with pytest.raises(ValueError):
        validator.validate(parts)


def test_validator_rejects_negative_weight():
    parts = [
        Part("P001", "Vélo", None, 1, 0.0, "ASSEMBLY"),
        Part("P002", "Roue avant", "P001", 1, -1.2, "Aluminium"),
    ]

    validator = BomValidator()

    with pytest.raises(ValueError):
        validator.validate(parts)


def test_validator_rejects_unknown_parent():
    parts = [
        Part("P001", "Vélo", None, 1, 0.0, "ASSEMBLY"),
        Part("P002", "Roue avant", "UNKNOWN", 1, 1.2, "Aluminium"),
    ]

    validator = BomValidator()

    with pytest.raises(ValueError):
        validator.validate(parts)


def test_validator_rejects_invalid_quantity():
    parts = [
        Part("P001", "Vélo", None, 1, 0.0, "ASSEMBLY"),
        Part("P002", "Roue avant", "P001", 0, 1.2, "Aluminium"),
    ]

    validator = BomValidator()

    with pytest.raises(ValueError):
        validator.validate(parts)


def test_validator_rejects_self_parent():
    parts = [
        Part("P001", "Vélo", None, 1, 0.0, "ASSEMBLY"),
        Part("P002", "Roue avant", "P002", 1, 1.2, "Aluminium"),
    ]

    validator = BomValidator()

    with pytest.raises(ValueError):
        validator.validate(parts)


def test_validator_rejects_multiple_roots():
    parts = [
        Part("P001", "Vélo", None, 1, 0.0, "ASSEMBLY"),
        Part("P002", "Roue avant", None, 1, 1.2, "Aluminium"),
    ]

    validator = BomValidator()

    with pytest.raises(ValueError):
        validator.validate(parts)