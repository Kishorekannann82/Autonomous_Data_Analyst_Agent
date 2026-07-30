import pandas as pd


class OutlierDetector:
    """
    Detects outliers in continuous numerical columns
    using the Interquartile Range (IQR) method.
    """

    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def get_continuous_columns(self):
        """
        Returns only continuous numerical columns.
        Ignores binary and low-cardinality numeric columns.
        """

        continuous_columns = []

        numerical_columns = self.df.select_dtypes(
            include=["number"]
        ).columns

        for column in numerical_columns:

            if self.df[column].nunique(dropna=True) > 15:
                continuous_columns.append(column)

        return continuous_columns

    def detect_outliers(self):

        report = {}

        for column in self.get_continuous_columns():

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

                "lower_bound": round(lower_bound, 2),

                "upper_bound": round(upper_bound, 2),

                "outlier_count": len(outliers),

                "outlier_percentage": round(
                    len(outliers) / len(self.df) * 100,
                    2
                )
            }

        return report

    def generate_report(self):

        return {

            "status": "success",

            "result": self.detect_outliers()
        }