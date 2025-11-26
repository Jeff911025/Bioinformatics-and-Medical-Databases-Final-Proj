import pandas as pd
import sqlite3



if __name__ == "__main__":
        
    csv_path = "COA_OpenData.csv"
    db_path = "test.db"
    df = pd.read_csv(csv_path, encoding="utf-8")
    con = sqlite3.connect(db_path)


    animal_df = df[[
        "animal_id",
        "animal_subid",
        "animal_area_pkid",
        "animal_shelter_pkid",
        "animal_place",
        "animal_kind",
        "animal_Variety",
        "animal_sex",
        "animal_bodytype", 
        "animal_colour",
        "animal_age",
        "animal_sterilization",
        "animal_bacterin",
        "animal_foundplace",
        "animal_title",
        "animal_status",
        "animal_remark",
        "animal_caption",
        "animal_opendate"

    ]].copy()

    animal_df = animal_df.rename(columns={
        "animal_shelter_pkid": "shelter_id",
        "animal_bodytype": "body_type",
        "animal_colour": "colour",
        "animal_age": "age"
    })

    animal_df.to_sql(
        "Animal",
        con,
        if_exists="append",
        index=False
    )
