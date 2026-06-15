from bom_extractor.domain.services.weight_service import WeightCalculationService
from bom_extractor.models import Part


def test_calculate_total_weight_for_assembly():
    parts = [
        Part("P001", "Vélo", None, 1, 0.0, "ASSEMBLY"),
        Part("P002", "Roue avant", "P001", 1, 1.2, "Aluminium"),
        Part("P003", "Cadre", "P001", 1, 2.5, "Acier"),
        Part("P004", "Pneu avant", "P002", 1, 0.7, "Caoutchouc"),
        Part("P005", "Jante avant", "P002", 1, 0.5, "Aluminium"),
    ]

    service = WeightCalculationService()

    total_weight = service.calculate_total_weight("P001", parts)

    assert total_weight == 4.9