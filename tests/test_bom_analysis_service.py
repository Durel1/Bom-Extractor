from bom_extractor.domain.services.bom_analysis_service import BomAnalysisService
from bom_extractor.models import Part


def create_sample_bom():
    return [
        Part("P001", "Vélo", None, 1, 0.0, "ASSEMBLY"),
        Part("P002", "Roue avant", "P001", 1, 1.2, "Aluminium"),
        Part("P003", "Cadre", "P001", 1, 2.5, "Acier"),
        Part("P004", "Pneu avant", "P002", 1, 0.7, "Caoutchouc"),
        Part("P005", "Jante avant", "P002", 1, 0.5, "Aluminium"),
    ]

def test_count_parts():
    service = BomAnalysisService()

    count = service.count_parts(create_sample_bom())

    assert count == 5


def test_get_materials():
    service = BomAnalysisService()

    materials = service.get_materials(create_sample_bom())

    assert materials == {
        "ASSEMBLY",
        "Aluminium",
        "Acier",
        "Caoutchouc"
    }


def test_count_parts_by_material():
    service = BomAnalysisService()

    result = service.count_parts_by_material(create_sample_bom())

    assert result["Aluminium"] == 2
    assert result["Acier"] == 1
    assert result["Caoutchouc"] == 1


def test_get_tree_depth():
    service = BomAnalysisService()

    depth = service.get_tree_depth(
        "P001",
        create_sample_bom()
    )

    assert depth == 3