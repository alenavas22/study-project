import os
import pandas as pd

import gdown


def download_data(file_id: str, file_name: str) -> None:
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        gdown.download(id=file_id, output=file_name)


def read_data(file_path: str) -> pd.DataFrame:
    print("Чтение csv файла")
    data = pd.read_csv(file_path)
    return data
