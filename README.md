資料庫來源:https://data.gov.tw/dataset/85903

步驟:

0.必須先建好Schema再執行以下，否則無法指定屬性類別以及主要鍵、外來鍵

1.utils\load_animal_to_sql.py

2.utils\load_area_to_sql.py

3.utils\load_shelter_to_sql.py

4.玩你的查詢指令

### Requirements:

`<ins>`主鍵 `</ins>`、*外來鍵*

- Animal(動物)

  `<ins>`animal_id `</ins>` (動物的流水編號)、animal_subid(動物的收容編號)、animal_area_pkid(動物所屬縣市代碼)、animal_shelter_pkid(動物所屬收容所代碼)、animal_place(動物的實際所在地)、animal_kind(動物的類型)、animal_Variety(動物品種)、animal_sex(動物性別)、animal_bodytype(動物體型)、animal_colour(動物毛色)、animal_age(動物年紀)、animal_sterilization(是否絕育)、animal_bacterin(是否施打狂犬病疫苗)、animal_foundplace(動物尋獲地)、animal_title(動物網頁標題)、animal_status(動物狀態)、animal_remark(資料備註)、animal_caption(其他說明)、animal_opendate(開放認養時間(起))、animal_closeddate(開放認養時間(迄))、animal_update(動物資料異動時間)、animal_createtime(動物資料建立時間)、adoption_date、*shelter_name*、*adopter_id*
- Shelter(收容所)

  `<ins>`shelter_name `</ins>` (動物所屬收容所名稱)、album_file(圖片名稱)、album_update(異動時間)、cDate(資料更新時間)、shelter_address(地址)、shelter_tel(連絡電話)
- Adopter(領養者)

  `<ins>`adopter_id `</ins>` adopter_name、adopter_phone、adopter_email、adopter_city、adopter_age、adopter_house_type

  `</ins>`adopter_id `</ins>`還沒有在.csv中，應該是要在load_adopter_to_sql.py自動依序指派，#TODO

盈利12.08 v2修改
初始化資料庫

1. 執行 recreate_db.py ，該程式會刪除並重新建立乾淨 test.db 檔案
2. 到 schema.sql > 右鍵 > Use Database > 選擇 test.db
3. 到 schema.sql > 右鍵 Run Query
4. 執行 utils\load.py
5. 到 new_query.sql > 右鍵 > Use Database > 選擇 test.db
6. 至此資料庫初始化完成

執行查詢

> 在 new_query.sql 打指令 > 右鍵 Run Query

修改方式

> 改動 schma.sql 跟 column_map.json，調整schma設計跟對照表
>
> adopter phone 需要另外處置(原有問題：panda讀取的自動判斷型別導致變成float，並保留第一筆 null。 已經修正。)

優點/動機

1. 初始化只要執行一個py檔案。大部分欄位不用一一指定，只有特定欄位需要。(例如當adopter phone出現問題時要另外調整)
2. 對照表放在column_map.json方便檢視修改。
3. 原先疑似是py檔案中的to_sql語法直接建立schema，而非透過sql指令，邏輯怪怪，理想中py檔案只負責插入工作，建立是由sql指令負責。

> 證明: 刪除test.db > 新增乾淨test.db檔案 > 執行 utils\load_animal_to_sql.py
> VS code介面左側 test.db檔案右鍵 > New Query > 在新的檔案中寫 SELECT * FROM Animal; > 右鍵 Run Query > 一樣顯示，這個過程沒有用到-- SQLite.sql
