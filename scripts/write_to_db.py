import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

def write_to_db():
    load_dotenv()

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_url = os.getenv("DB_URL")
    db_port = os.getenv("DB_PORT")
    db_root_base = os.getenv("DB_NAME")

    df = pd.read_parquet("dataset.parquet")

    data_100_rows = df.head(100)

    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_root_base}",
        pool_recycle=3600,
    )

    table_name = "vasilenkoav"

    data_100_rows.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print("100 строк датасета записаны в удаленную базу данных")

if __name__ == "__main__":
    write_to_db()
