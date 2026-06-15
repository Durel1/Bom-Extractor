from bom_extractor.models import Part


class BomValidator:
    """
    Validates business rules for a Bill of Materials.

    The validator checks data consistency before inserting parts
    into the database.
    """

    def validate(self, parts: list[Part]) -> None:
        self._check_no_duplicate_ids(parts)
        self._check_positive_quantities(parts)
        self._check_no_negative_weights(parts)
        self._check_existing_parents(parts)
        self._check_no_self_parent(parts)
        self._check_single_root(parts)

    def _check_no_duplicate_ids(self, parts: list[Part]) -> None:
        seen_ids = set()

        for part in parts:
            if part.part_id in seen_ids:
                raise ValueError(f"Duplicate part ID found: {part.part_id}")
            seen_ids.add(part.part_id)

    def _check_positive_quantities(self, parts: list[Part]) -> None:
        for part in parts:
            if part.quantity <= 0:
                raise ValueError(f"Quantity must be positive for part {part.part_id}")

    def _check_no_negative_weights(self, parts: list[Part]) -> None:
        for part in parts:
            if part.unit_weight < 0:
                raise ValueError(f"Weight cannot be negative for part {part.part_id}")

    def _check_existing_parents(self, parts: list[Part]) -> None:
        existing_ids = {part.part_id for part in parts}

        for part in parts:
            if part.parent_id is not None and part.parent_id not in existing_ids:
                raise ValueError(f"Parent ID does not exist: {part.parent_id}")

    def _check_no_self_parent(self, parts: list[Part]) -> None:
        for part in parts:
            if part.parent_id == part.part_id:
                raise ValueError(f"Part cannot be its own parent: {part.part_id}")

    def _check_single_root(self, parts: list[Part]) -> None:
        root_parts = [part for part in parts if part.parent_id is None]

        if len(root_parts) != 1:
            raise ValueError("A BOM must have exactly one root part")