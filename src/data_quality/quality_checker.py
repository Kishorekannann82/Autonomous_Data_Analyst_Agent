import pandas as pd

from missing_value_checker import MissingValueChecker
from duplicate_checker import DuplicateChecker
from outlier_detector import OutlierDetector
from constant_column_checker import ConstantColumnChecker
from datatype_checker import DatatypeChecker
from unique_value_checker import UniqueValueChecker
from invalid_value_checker import InvalidValueChecker


class QualityChecker:

    CHECKERS = [

        MissingValueChecker,

        DuplicateChecker,

        OutlierDetector,

        ConstantColumnChecker,

        DatatypeChecker,

        UniqueValueChecker,

        InvalidValueChecker

    ]

    def __init__(self, file_path):

        self.df = pd.read_csv(file_path)

    def run_checkers(self):

        report = {}

        for checker in self.CHECKERS:

            checker_instance = checker(self.df)

            checker_name = checker.__name__.replace(
                "Checker",
                ""
            ).replace(
                "Detector",
                ""
            ).lower()

            report[checker_name] = checker_instance.generate_report()

        return report

    def calculate_quality_score(self, report):

        score = 100

        # Missing Values
        missing = report["missingvalue"]["result"]["missing_percentage"]

        score -= min(sum(missing.values()), 30)

        # Duplicate Rows
        duplicates = report["duplicate"]["result"]["duplicate_count"]

        score -= min(duplicates, 20)

        # Constant Columns
        constants = report["constantcolumn"]["result"]["constant_columns"]

        score -= len(constants) * 5

        return max(round(score, 2), 0)

    def generate_report(self):

        report = self.run_checkers()

        report["quality_score"] = self.calculate_quality_score(
            report
        )

        return report