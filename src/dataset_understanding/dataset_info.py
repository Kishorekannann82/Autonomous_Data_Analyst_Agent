from pprint import pprint
from dataset_profiler import DatasetProfiler
from metadata import MetadataManager
if __name__ == "__main__":
    profiler = DatasetProfiler(
        "../../datasets/raw/finance/loan_prediction.csv"
    )
    metadata = profiler.generate_metadata()

    pprint(metadata)

    metadata_manager = MetadataManager()

    metadata_manager.save_metadata(metadata)