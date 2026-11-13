import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine
from sqlalchemy.engine import URL


def save_data(data: pd.DataFrame, output_path: str) -> None:
    print("Запись файла в правильный формат")
    data.to_parquet(output_path, index=False)


def write_to_db(parquet_path: str = "dataset.parquet") -> tuple[Engine, str]:
    """Запись 100 строк датасета в удаленную базу данных"""
    load_dotenv()

    missing = [
        k
        for k in ("DB_USER", "DB_PASSWORD", "DB_URL", "DB_PORT", "DB_NAME")
        if not os.getenv(k)
    ]
    if missing:
        raise RuntimeError(f"Нет переменных в .env: {', '.join(missing)}")

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_url = os.getenv("DB_URL")
    db_port = os.getenv("DB_PORT")
    db_root_base = os.getenv("DB_NAME")

    df = pd.read_parquet(parquet_path)

    data_100_rows = df.head(100)

    url = URL.create(
        "postgresql+psycopg2",
        username=db_user,
        password=db_password,
        host=db_url,
        port=int(db_port),
        database=db_root_base,
    )

    engine = create_engine(url, pool_recycle=3600)

    table_name = "vasilenkoav"

    data_100_rows.to_sql(name=table_name, con=engine, if_exists="replace", index=False)

    return engine, table_name


def validate_db_data(engine: Engine, table_name: str) -> bool:
    """Проверка записи таблицы в базу данных"""
    df_check = pd.read_sql_table(table_name, con=engine)
    return len(df_check) == 100
