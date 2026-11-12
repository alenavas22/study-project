import csv
from itertools import islice
import os
import pandas as pd

import gdown

# Открывает csv-файл и выводит первые 10 строк


def show_data(file: str, n: int = 10) -> None:
    print(f"Первые {n} строк датасета")
    with open(file, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        for line in islice(reader, n):
            print(line)


# Читает csv-файл


def read_data(file_path: str) -> pd.DataFrame:
    print("Чтение csv файла")
    data = pd.read_csv(file_path)
    return data


# Приводит типы данных


def data_types(data: pd.DataFrame) -> pd.DataFrame:
    print("Приведение типа данных")

    data["Has_OMS"] = data["Has_OMS"] == "Yes"
    data["FSR_overlap"] = data["FSR_overlap"] == "Y"
    data["from_CSD"] = data["from_CSD"] == "Y"
    data["public"] = data["public"] == "Y"
    data["CSD_overlap_inCoRE"] = data["CSD_overlap_inCoRE"] == "Y"
    data["CSD_overlap_inCCDC"] = data["CSD_overlap_inCCDC"] == "Y"

    data = data.astype(
        {
            "filename": "str",
            "Open_Metal_Sites": "str",
            "DISORDER": "str",
            "CSD_of_WoS_inCoRE": "str",
            "date_CSD": "str",
            "DOI_public": "str",
            "Note": "str",
            "LCD": "float32",
            "PLD": "float32",
            "LFPD": "float32",
            "cm3_g": "float32",
            "ASA_m2_cm3": "float32",
            "ASA_m2_g": "float32",
            "NASA_m2_cm3": "float32",
            "NASA_m2_g": "float32",
            "AV_VF": "float32",
            "AV_cm3_g": "float32",
            "NAV_cm3_g": "float32",
            "All_Metals": "category",
            "Matched_CSD_of_CoRE": "category",
            "Possible_List_CSD_of_CoRE": "category",
            "Extension": "category",
            "Has_OMS": "bool",
            "FSR_overlap": "bool",
            "from_CSD": "bool",
            "public": "bool",
            "CSD_overlap_inCoRE": "bool",
            "CSD_overlap_inCCDC": "bool",
        }
    )
    return data


# Записывает файл в формат parquet


def save_data(data: pd.DataFrame, output_path: str) -> None:
    print("Запись файла в правильный формат")
    data.to_parquet(output_path, index=False)


if __name__ == "__main__":
    FILE_ID = "1VtPmObnfUbxaKAvi0SEaLBdVvYJSNMHV"
    FILE_NAME = "dataset.csv"
    PARQUET_NAME = "dataset.parquet"

    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        gdown.download(id=FILE_ID, output=FILE_NAME)

    show_data(FILE_NAME)

    if not os.path.exists(PARQUET_NAME) or os.path.getsize(PARQUET_NAME) == 0:
        data = read_data(FILE_NAME)
        data = data_types(data)
        save_data(data, PARQUET_NAME)
