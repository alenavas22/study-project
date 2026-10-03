import csv
from itertools import islice
import os

import gdown


def show_data(file: str, n: int = 10) -> None:
    print(f"Первые {n} строк датасета")
    with open(file, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for line in islice(reader, n):
            print(line)


if __name__ == "__main__":
    file_id = "1VtPmObnfUbxaKAvi0SEaLBdVvYJSNMHV"
    file_name = "dataset.csv"

    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        gdown.download(id=file_id, output=file_name)

    show_data(file_name)
