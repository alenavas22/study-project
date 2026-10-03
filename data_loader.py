import csv
from itertools import islice
import os
import gdown


def show_data(file, n=10):
    print(f"Первые {n} строк датасета")
    with open(file, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for line in islice(reader, n):
            print(line)


if __name__ == "__main__":
    link = "https://drive.google.com/uc?id=1VtPmObnfUbxaKAvi0SEaLBdVvYJSNMHV"
    file_name = "dataset.csv"

    if not os.path.exists(file_name):
        gdown.download(link, file_name)

    show_data(file_name)
