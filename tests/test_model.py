from bom_extractor.models import Part


def test_create_part():
    part = Part(
        part_id="P001",
        name="Vélo",
        parent_id=None,
        quantity=1,
        unit_weight=0.0,
        material="ASSEMBLY"
    )

    assert part.part_id == "P001"
    assert part.name == "Vélo"
    assert part.parent_id is None
    assert part.quantity == 1
    assert part.unit_weight == 0.0
    assert part.material == "ASSEMBLY"