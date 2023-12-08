from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class EvaluationConfig:
    root_dir: Path
    model_path: Path
    test_data_path: Path
    lables_data_path: Path
    metric_file_name: Path
    mlflow_uri: str
    