import pandas as pd
import sqlite3
import json

COLUMN_MAP_FILE = "column_map.json"
CSV_PATH = "COA_OpenData_with_adopter.csv"
DB_PATH = "test.db"


def load_mapping(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def check_schema(cursor, table_name, mapped_columns):
    cursor.execute(f"PRAGMA table_info({table_name})")
    sql_columns = [row[1] for row in cursor.fetchall()]

    missing = set(sql_columns) - set(mapped_columns)
    extra = set(mapped_columns) - set(sql_columns)
    if missing:
        print(f"⚠ SQL 表格 {table_name} 有欄位沒映射到 CSV:", missing)
    if extra:
        print(f"⚠ CSV 欄位映射在表 {table_name} 但 SQL 沒有:", extra)


def insert_table(cursor, df, mapping, table_name, key_field=None):
    data = df.to_dict(orient='records')

    sql_columns = list(mapping.values())
    csv_columns = list(mapping.keys())

    sql = f"""
        INSERT OR REPLACE INTO {table_name} ({", ".join(sql_columns)})
        VALUES ({", ".join(":"+col for col in csv_columns)})
    """

    cursor.executemany(sql, data)


if __name__ == "__main__":
    df = pd.read_csv(CSV_PATH, encoding="utf-8")
    mapping = load_mapping(COLUMN_MAP_FILE)

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    # ========== Animal ==========
    animal_map = mapping["Animal"]
    check_schema(cur, "Animal", animal_map.values())
    animal_df = df[animal_map.keys()].copy()
    insert_table(cur, animal_df, animal_map, "Animal")

    # ========== animal_remark ==========
    remark_map = mapping["animal_remark"]
    remark_df = df[remark_map.keys()].copy()

    # 去掉 remark 為 null 的列
    remark_df = remark_df[remark_df["animal_remark"].notna()]
    insert_table(cur, remark_df, remark_map, "animal_remark")

    # ========== Shelter ==========
    shelter_map = mapping["Shelter"]
    shelter_df = df[shelter_map.keys()].drop_duplicates(subset=["animal_shelter_pkid"])
    insert_table(cur, shelter_df, shelter_map, "Shelter")

    # ========== Adopter ==========
    adopter_map = mapping["Adopter"]
    adopter_df = df[adopter_map.keys()].drop_duplicates(subset=["adopter_phone"])
    insert_table(cur, adopter_df, adopter_map, "Adopter")

    con.commit()
    con.close()

    print("🎉 匯入完成！")
