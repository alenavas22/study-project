import pandas as pd
from sqlalchemy import create_engine

def read_creds():
    engine = create_engine("sqlite:///creds.db")
    df = pd.read_sql_table("access", con=engine)
    print(df)

if __name__ == "__main__":
    read_creds()
