from pathlib import Path
import pandas as pd

class DatasetProfiler:
    def __init__(self,file_path):
        self.file_path=file_path
        self.df=pd.read_csv(file_path)
    def get_basic_info(self):
        return {
            "dataset_name":Path(self.file_path).stem,
            "rows":self.df.shape[0],
            "columns":self.df.shape[1]
        }
    def get_feature_types(self):
        numerical=self.df.select_dtypes(
            include=["int64","float64"]
        ).columns.tolist()
        categorical=self.df.select_dtypes(
            include=["object"]
        ).columns.tolist()
        return {
            "numerical_features":numerical,
            "categorical_features":categorical
        }
    def get_missing_values(self):
        missing=self.df.isnull().sum()
        return missing[missing>0].to_dict()
    def get_duplicate_count(self):
        return int(self.df.duplicated().sum())
    def profile(self):
        return {
            **self.get_basic_info(),
            **self.get_feature_types(),
            "missing_values":self.get_missing_values(),
            "duplicates":self.get_duplicate_count()
        }
        