import sys
from etl.extract import download_data, read_data
from etl.transform import data_types, validate_data
from etl.load import save_data, write_to_db, validate_db_data

FILE_ID = "1VtPmObnfUbxaKAvi0SEaLBdVvYJSNMHV"
PARQUET_NAME = "dataset.parquet"


def main():
    file_name = sys.argv[1] if len(sys.argv) > 1 else "dataset.csv"

    # Extract
    download_data(FILE_ID, file_name)
    data = read_data(file_name)

    # Transform
    data = data_types(data)
    if not validate_data(data):
        raise ValueError("Обнаружены ошибки в данных после преобразования типов.")

    # Load
    save_data(data, PARQUET_NAME)
    engine, table_name = write_to_db(PARQUET_NAME)
    if not validate_db_data(engine, table_name):
        raise ValueError(
            "Ошибка записи в базу данных. Количество строк в таблице не равно 100."
        )

    print("100 строк датасета записаны в удаленную базу данных.")


if __name__ == "__main__":
    main()
