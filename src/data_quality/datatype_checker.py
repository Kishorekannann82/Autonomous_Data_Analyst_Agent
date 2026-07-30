import pandas as pd


class DatatypeChecker:
    """
    Identifies datatype and logical category of each column.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def classify_column(self, column):

        dtype = self.df[column].dtype

        unique_count = self.df[column].nunique(dropna=True)

        if column.lower().endswith("_id"):

            return "Identifier"

        if pd.api.types.is_numeric_dtype(dtype):

            if unique_count <= 15:
                return "Categorical"

            return "Numerical"

        if pd.api.types.is_datetime64_any_dtype(dtype):

            return "Datetime"

        return "Categorical"

    def get_datatypes(self):

        report = {}

        for column in self.df.columns:

            report[column] = {

                "datatype": str(self.df[column].dtype),

                "category": self.classify_column(column)

            }

        return report

    def generate_report(self):

        return {

            "status": "success",

            "result": self.get_datatypes()

        }