from dataclasses import dataclass
from typing import Optional


@dataclass
class Part:
    """
    Represents a mechanical part in a Bill of Materials.

    A part can be a final product, an assembly, or a component.
    parent_id is None when the part is the root of the BOM.
    """
    part_id: str
    name: str
    parent_id: Optional[str]
    quantity: int
    unit_weight: float
    material: str