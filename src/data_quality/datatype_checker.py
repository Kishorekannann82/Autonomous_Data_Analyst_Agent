import pandas as pd


class DatatypeChecker:
    """
    Summarizes column data types.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def get_datatypes(self):

        report = {}

        for column in self.df.columns:

            report[column] = str(self.df[column].dtype)

        return report

    def generate_report(self):

        return {
            "status": "success",
            "result": self.get_datatypes()
        }