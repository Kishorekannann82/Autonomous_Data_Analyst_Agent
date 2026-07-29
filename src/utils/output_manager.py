from pathlib import Path


class OutputManager:
    """
    Creates and manages all output folders.
    """

    OUTPUT_DIRS = [
        "metadata",
        "profiles",
        "reports",
        "visualizations",
        "logs"
    ]

    def __init__(self, base_path="../../outputs"):

        self.base_path = Path(base_path)

        self.create_output_directories()

    def create_output_directories(self):

        for folder in self.OUTPUT_DIRS:

            path = self.base_path / folder

            path.mkdir(
                parents=True,
                exist_ok=True
            )

    def get_output_path(self, folder_name):
        return self.base_path / folder_name