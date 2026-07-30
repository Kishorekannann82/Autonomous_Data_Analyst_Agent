import pandas as pd


class UniqueValueChecker:
    """
    Counts unique values for each column.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def get_unique_values(self):

        report = {}

        for column in self.df.columns:

            report[column] = int(
                self.df[column].nunique(dropna=True)
            )

        return report

    def generate_report(self):

        return {
            "status": "success",
            "result": self.get_unique_values()
        }