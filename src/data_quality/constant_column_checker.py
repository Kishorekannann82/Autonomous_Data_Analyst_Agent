import pandas as pd


class ConstantColumnChecker:
    """
    Identifies columns with only one unique value.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def get_constant_columns(self):

        constant_columns = []

        for column in self.df.columns:

            if self.df[column].nunique(dropna=True) <= 1:
                constant_columns.append(column)

        return constant_columns

    def generate_report(self):

        return {
            "status": "success",
            "result": {
                "constant_columns": self.get_constant_columns()
            }
        }