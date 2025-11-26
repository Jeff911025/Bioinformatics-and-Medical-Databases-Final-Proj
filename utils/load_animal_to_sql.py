import pandas as pd
import sqlite3
#animal_place(動物的實際所在地)
#animal_kind(動物的類型)
#animal_Variety(動物品種)
#animal_sex(動物性別)
#animal_bodytype(動物體型)
#animal_colour(動物毛色)
#animal_age(動物年紀)
#animal_sterilization(是否絕育)
#animal_bacterin(是否施打狂犬病疫苗)
#animal_foundplace(動物尋獲地)
#animal_title(動物網頁標題)
#animal_status(動物狀態)
#animal_remark(資料備註)
#animal_caption(其他說明)
#animal_opendate(開放認養時間(起))
#animal_closeddate(開放認養時間(迄))
#animal_update(動物資料異動時間)
#animal_createtime(動物資料建立時間)
#album_file(圖片名稱)
#album_update(異動時間)
#cDate(資料更新時間)


if __name__ == "__main__":
        
    csv_path = "COA_OpenData.csv"
    db_path = "test.db"
    df = pd.read_csv(csv_path, encoding="utf-8")
    con = sqlite3.connect(db_path)


    animal_df = df[[
        "animal_id",
        "animal_subid",
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
        "animal_opendate",
        "animal_closeddate",
        "animal_update",
        "animal_createtime",
        "album_file",
        "album_update",
        "cDate"

    ]].copy()

    # animal_df = animal_df.rename(columns={
        
    # })

    animal_df.to_sql(
        "Animal",
        con,
        if_exists="append",
        index=False
    )