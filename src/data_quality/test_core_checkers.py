from pprint import pprint
import pandas as pd

from missing_value_checker import MissingValueChecker
from duplicate_checker import DuplicateChecker
from outlier_detector import OutlierDetector
from constant_column_checker import ConstantColumnChecker
from datatype_checker import DatatypeChecker
from unique_value_checker import UniqueValueChecker
from invalid_value_checker import InvalidValueChecker


df = pd.read_csv("../../datasets/raw/finance/loan_prediction.csv")

checkers = [
    ("Missing Value Checker", MissingValueChecker(df)),
    ("Duplicate Checker", DuplicateChecker(df)),
    ("Outlier Detector", OutlierDetector(df)),
    ("Constant Column Checker", ConstantColumnChecker(df)),
    ("Datatype Checker", DatatypeChecker(df)),
    ("Unique Value Checker", UniqueValueChecker(df)),
    ("Invalid Value Checker", InvalidValueChecker(df)),
]

for name, checker in checkers:
    print("=" * 60)
    print(name)
    print("=" * 60)
    pprint(checker.generate_report())
    print()