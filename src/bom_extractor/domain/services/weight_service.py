from bom_extractor.models import Part


class WeightCalculationService:
    """
    Calculates the total weight of an assembly from a BOM structure.
    """

    def calculate_total_weight(self, root_part_id: str, parts: list[Part]) -> float:
        children_by_parent = self._build_children_index(parts)
        return self._calculate_recursive(root_part_id, children_by_parent)

    def _build_children_index(self, parts: list[Part]) -> dict[str | None, list[Part]]:
        children_by_parent = {}

        for part in parts:
            children_by_parent.setdefault(part.parent_id, []).append(part)

        return children_by_parent

    def _calculate_recursive(
        self,
        part_id: str,
        children_by_parent: dict[str | None, list[Part]]
    ) -> float:
        total_weight = 0.0

        for child in children_by_parent.get(part_id, []):
            child_total_weight = child.unit_weight + self._calculate_recursive(
                child.part_id,
                children_by_parent
            )

            total_weight += child.quantity * child_total_weight

        return total_weight