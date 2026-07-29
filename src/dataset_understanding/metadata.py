from utils.output_manager import OutputManager
from utils.file_manager import FileManager
from utils.constants import METADATA_FOLDER


class MetadataManager:
    """
    Handles saving and loading dataset metadata.
    """

    def __init__(self):
        self.output_manager = OutputManager()

    def save_metadata(self, metadata: dict):
        """
        Save metadata as a JSON file.
        """

        dataset_name = metadata["dataset_name"]

        metadata_path = (
            self.output_manager.get_output_path(METADATA_FOLDER)
            / f"{dataset_name}.json"
        )

        FileManager.save_json(metadata, metadata_path)

        print("\n========================================")
        print(" Metadata saved successfully!")
        print(f" File : {metadata_path}")
        print("========================================\n")

    def load_metadata(self, dataset_name: str):
        """
        Load metadata JSON.
        """

        metadata_path = (
            self.output_manager.get_output_path(METADATA_FOLDER)
            / f"{dataset_name}.json"
        )

        return FileManager.load_json(metadata_path)