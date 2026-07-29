from pathlib import Path
import json


class FileManager:

    @staticmethod
    def save_json(data, file_path):

        file_path = Path(file_path)

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(file_path, "w", encoding="utf-8") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    @staticmethod
    def load_json(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return json.load(file)