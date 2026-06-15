from collections import Counter

from bom_extractor.models import Part


class BomAnalysisService:

    def count_parts(self, parts: list[Part]) -> int:
        return len(parts)

    def get_materials(self, parts: list[Part]) -> set[str]:
        return {part.material for part in parts}

    def count_parts_by_material(
        self,
        parts: list[Part]
    ) -> dict[str, int]:

        counter = Counter()

        for part in parts:
            counter[part.material] += 1

        return dict(counter)

    def get_tree_depth(
        self,
        root_part_id: str,
        parts: list[Part]
    ) -> int:

        children_by_parent = {}

        for part in parts:
            children_by_parent.setdefault(
                part.parent_id,
                []
            ).append(part)

        return self._depth(
            root_part_id,
            children_by_parent
        )

    def _depth(
        self,
        part_id: str,
        children_by_parent: dict
    ) -> int:

        children = children_by_parent.get(part_id, [])

        if not children:
            return 1

        return 1 + max(
            self._depth(
                child.part_id,
                children_by_parent
            )
            for child in children
        )