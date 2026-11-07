import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def write_to_db():
    load_dotenv()

    missing = [k for k in ("DB_USER", "DB_PASSWORD", "DB_URL", "DB_PORT", "DB_NAME") if not os.getenv(k)]
    if missing:
        raise RuntimeError(f"Нет переменных в .env: {', '.join(missing)}")

    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_url = os.getenv("DB_URL")
    db_port = os.getenv("DB_PORT")
    db_root_base = os.getenv("DB_NAME")
    
    df = pd.read_parquet("dataset.parquet")

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

    data_100_rows.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print("100 строк датасета записаны в удаленную базу данных")

if __name__ == "__main__":
    write_to_db()
