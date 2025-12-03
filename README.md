資料庫來源:https://data.gov.tw/dataset/85903

步驟:

0.必須先建好Schema再執行以下，否則無法指定屬性類別以及主要鍵、外來鍵

1.utils\load_animal_to_sql.py

2.utils\load_area_to_sql.py

3.utils\load_shelter_to_sql.py

4.玩你的查詢指令

### Requirements:

- Animal(動物)

  animal_id(動物的流水編號)、animal_subid(動物的收容編號)、animal_area_pkid(動物所屬縣市代碼)、animal_shelter_pkid(動物所屬收容所代碼)、animal_place(動物的實際所在地)、animal_kind(動物的類型)、animal_Variety(動物品種)、animal_sex(動物性別)、animal_bodytype(動物體型)、animal_colour(動物毛色)、animal_age(動物年紀)、animal_sterilization(是否絕育)、animal_bacterin(是否施打狂犬病疫苗)、animal_foundplace(動物尋獲地)、animal_title(動物網頁標題)、animal_status(動物狀態)、animal_remark(資料備註)、animal_caption(其他說明)、animal_opendate(開放認養時間(起))、animal_closeddate(開放認養時間(迄))、animal_update(動物資料異動時間)、animal_createtime(動物資料建立時間)

- Shelter(收容所)

  shelter_name(動物所屬收容所名稱)、album_file(圖片名稱)、album_update(異動時間)、cDate(資料更新時間)、shelter_address(地址)、shelter_tel(連絡電話)

- Adopter(領養者)
  ...
