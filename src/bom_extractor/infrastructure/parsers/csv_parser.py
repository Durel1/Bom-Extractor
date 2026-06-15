import pandas as pd

from bom_extractor.application.interfaces.parser import BomParser
from bom_extractor.models import Part


class CsvBomParser(BomParser):

    def parse(
        self,
        file_path: str
    ) -> list[Part]:

        dataframe = pd.read_csv(file_path)

        parts = []

        for _, row in dataframe.iterrows():

            parent_id = row["parent_id"]

            if pd.isna(parent_id):
                parent_id = None

            parts.append(
                Part(
                    part_id=str(row["part_id"]),
                    name=str(row["name"]),
                    parent_id=parent_id,
                    quantity=int(row["quantity"]),
                    unit_weight=float(row["unit_weight"]),
                    material=str(row["material"])
                )
            )

        return parts