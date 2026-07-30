import pandas as pd


class DuplicateChecker:
    """
    Checks duplicate rows in the dataset.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def get_duplicate_count(self):
        """
        Returns total duplicate rows.
        """
        return int(self.df.duplicated().sum())

    def get_duplicate_rows(self):
        """
        Returns all duplicate rows.
        """
        return self.df[self.df.duplicated()]

    def generate_report(self):
        """
        Generates duplicate report.
        """
        return {
            "status": "success",
            "result": {
                "duplicate_count": self.get_duplicate_count()
            }
        }