from pathlib import Path

PROJECT_NAME = "autonomous-data-analyst-agent"

folders = [
    "datasets/raw",
    "datasets/processed",
    "docs/dataset_notes",
    "docs/requirements",
    "src/dataset_understanding",
    "src/data_quality",
    "src/data_cleaning",
    "src/eda",
    "src/feature_engineering",
    "src/automl",
    "src/insights",
    "src/reporting",
    "src/chat_with_data",
    "tests",
    "reports",
    "notebooks",
    "app",
    "config",
]

root = Path(PROJECT_NAME)

for folder in folders:
    path = root / folder
    path.mkdir(parents=True, exist_ok=True)

    # create __init__.py for src modules
    if str(path).startswith(str(root / "src")):
        (path / "__init__.py").touch(exist_ok=True)

# Create root files
(root / "README.md").touch(exist_ok=True)
(root / ".gitignore").touch(exist_ok=True)
(root / "requirements.txt").touch(exist_ok=True)

print(f"✅ Project structure '{PROJECT_NAME}' created successfully!")