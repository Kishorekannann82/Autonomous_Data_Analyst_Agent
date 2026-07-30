from pprint import pprint
import pandas as pd

from missing_value_checker import MissingValueChecker
from duplicate_checker import DuplicateChecker
from outlier_detector import OutlierDetector


df = pd.read_csv("../../datasets/raw/finance/loan_prediction.csv")

print("=" * 60)
print("Missing Value Checker")
print("=" * 60)

pprint(
    MissingValueChecker(df).generate_report()
)

print()

print("=" * 60)
print("Duplicate Checker")
print("=" * 60)

pprint(
    DuplicateChecker(df).generate_report()
)

print()

print("=" * 60)
print("Outlier Detector")
print("=" * 60)

pprint(
    OutlierDetector(df).generate_report()
)