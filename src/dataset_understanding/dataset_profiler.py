from pathlib import Path
import pandas as pd
import os


class DatasetProfiler:

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.df = pd.read_csv(self.file_path)

    # -----------------------------
    # Basic Dataset Information
    # -----------------------------
    def get_dataset_name(self):
        return self.file_path.stem

    def get_shape(self):
        return {
            "rows": self.df.shape[0],
            "columns": self.df.shape[1]
        }

    def get_file_size(self):
        size = os.path.getsize(self.file_path)
        return round(size / 1024, 2)  # KB

    def get_memory_usage(self):
        memory = self.df.memory_usage(deep=True).sum()
        return round(memory / 1024, 2)  # KB

    # -----------------------------
    # Column Information
    # -----------------------------
    def get_column_names(self):
        return self.df.columns.tolist()

    def get_data_types(self):
        return self.df.dtypes.astype(str).to_dict()

    # -----------------------------
    # Feature Information
    # -----------------------------
    def get_feature_summary(self):

        numerical = self.df.select_dtypes(
            include=["int64", "float64"]
        ).columns.tolist()

        categorical = self.df.select_dtypes(
            include=["object"]
        ).columns.tolist()

        datetime = self.df.select_dtypes(
            include=["datetime64"]
        ).columns.tolist()

        return {
            "numerical": numerical,
            "categorical": categorical,
            "datetime": datetime
        }

    # -----------------------------
    # Data Quality Overview
    # -----------------------------
    def get_missing_values(self):
        missing = self.df.isnull().sum()
        return missing[missing > 0].to_dict()

    def get_duplicate_rows(self):
        return int(self.df.duplicated().sum())

    # -----------------------------
    # Generate Metadata
    # -----------------------------
    def generate_metadata(self):

        metadata = {
            "dataset_name": self.get_dataset_name(),
            "shape": self.get_shape(),
            "file_size_kb": self.get_file_size(),
            "memory_usage_kb": self.get_memory_usage(),
            "column_names": self.get_column_names(),
            "data_types": self.get_data_types(),
            "feature_summary": self.get_feature_summary(),
            "missing_values": self.get_missing_values(),
            "duplicate_rows": self.get_duplicate_rows()
        }

        return metadata