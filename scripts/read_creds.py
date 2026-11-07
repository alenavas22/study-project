import pandas as pd
from sqlalchemy import create_engine

def read_creds():
    try:
        engine = create_engine("sqlite:///creds.db")
        df = pd.read_sql_table("access", con=engine)
        print(df)
    except Exception as e:
        print(f"Ошибка: файл creds.db не найден или поврежден: {e}")

if __name__ == "__main__":
    read_creds()
