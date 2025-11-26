import pandas as pd
import sqlite3

if __name__ == "__main__":
    csv_path = "COA_OpenData_with_adopter.csv"
    db_path = "test.db"
    df = pd.read_csv(csv_path, encoding="utf-8")
    con = sqlite3.connect(db_path)

    adopter_df = df[[
        "adoption_date","adopter_name","adopter_phone","adopter_email","adopter_city","adopter_age","adopter_house_type"

    ]].copy()

    # adopter_df = adopter_df.rename(columns={
        
    # })

    adopter_df.to_sql(
        "Adopter",
        con,
        if_exists="append",
        index=False
    )