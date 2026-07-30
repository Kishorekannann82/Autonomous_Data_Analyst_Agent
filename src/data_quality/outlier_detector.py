import pandas as pd


class OutlierDetector:
    """
    Detects outliers using the IQR method.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def detect_outliers(self):
        """
        Detect outliers for each numerical column.
        """

        report = {}

        numerical_columns = self.df.select_dtypes(
            include=["number"]
        ).columns

        for column in numerical_columns:

            q1 = self.df[column].quantile(0.25)
            q3 = self.df[column].quantile(0.75)

            iqr = q3 - q1

            lower_bound = q1 - (1.5 * iqr)
            upper_bound = q3 + (1.5 * iqr)

            outliers = self.df[
                (self.df[column] < lower_bound) |
                (self.df[column] > upper_bound)
            ]

            report[column] = {
                "outlier_count": len(outliers),
                "outlier_percentage": round(
                    (len(outliers) / len(self.df)) * 100,
                    2
                )
            }

        return report

    def generate_report(self):
        """
        Generates outlier report.
        """
        return {
            "status": "success",
            "result": self.detect_outliers()
        }