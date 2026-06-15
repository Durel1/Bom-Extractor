import pandas as pd

from bom_extractor.models import Part


class BomCsvParser:
    """
    Reads a BOM CSV file and converts each row into a Part object.
    """

    def parse(self, file_path: str) -> list[Part]:
        dataframe = pd.read_csv(file_path)

        parts = []

        for _, row in dataframe.iterrows():
            parent_id = row["parent_id"]

            if pd.isna(parent_id):
                parent_id = None

            part = Part(
                part_id=str(row["part_id"]),
                name=str(row["name"]),
                parent_id=parent_id,
                quantity=int(row["quantity"]),
                unit_weight=float(row["unit_weight"]),
                material=str(row["material"]),
            )

            parts.append(part)

        return parts