import pandas as pd


class MissingValueChecker:
    """
    Checks missing values in the dataset.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def get_missing_count(self):
        """
        Returns the count of missing values for each column.
        """
        missing = self.df.isnull().sum()
        return missing[missing > 0].to_dict()

    def get_missing_percentage(self):
        """
        Returns the percentage of missing values for each column.
        """
        percentage = (
            self.df.isnull()
            .mean()
            .mul(100)
            .round(2)
        )

        return percentage[percentage > 0].to_dict()

    def generate_report(self):
        """
        Generates the missing value report.
        """
        return {
            "status": "success",
            "result": {
                "missing_count": self.get_missing_count(),
                "missing_percentage": self.get_missing_percentage()
            }
        }