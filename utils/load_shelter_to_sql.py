# animal_shelter_pkid(動物所屬收容所代碼)
# shelter_name(動物所屬收容所名稱)
# animal_area_pkid(動物所屬縣市代碼)
# shelter_address(地址)
# shelter_tel(連絡電話)
import pandas as pd
import sqlite3

if __name__ == "__main__":
    csv_path = "COA_OpenData.csv"
    db_path = "test.db"
    df = pd.read_csv(csv_path, encoding="utf-8")
    con = sqlite3.connect(db_path)