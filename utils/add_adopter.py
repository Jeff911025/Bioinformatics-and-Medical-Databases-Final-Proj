import pandas as pd
import numpy as np
import random

# === 可調參數 ===
INPUT_CSV = "COA_OpenData.csv"                # 原始 CSV 檔名
OUTPUT_CSV = "COA_OpenData_with_adopter.csv"  # 輸出的 CSV 檔名
ADOPTION_RATE = 0.4                       # 有多少比例的動物被視為「已被領養」
MAX_DAYS_AFTER_OPEN = 60                  # 領養日會落在 opendate 之後 1 ~ 60 天

# 一些簡單的假資料池，可以自己改
ADOPTER_NAMES = [
    "王小明", "陳怡君", "張家豪", "林俊宇", "李雅婷",
    "吳宗憲", "黃冠中", "趙子龍", "周芷若", "鄭元暢"
]
CITIES = ["台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市", "新竹市", "基隆市"]
HOUSE_TYPES = ["公寓", "大樓華廈", "透天厝", "有庭院", "頂樓加蓋"]


def random_phone():
    # 台灣手機格式 09XXXXXXXX
    return "09" + "".join(str(random.randint(0, 9)) for _ in range(8))


def random_email(name_index: int):
    domains = ["example.com", "test.com", "mail.com"]
    return f"user{name_index}@{random.choice(domains)}"


def gen_adoption_date(open_date: pd.Timestamp):
    """根據 animal_opendate 產生 adoption_date。
    - 有機率不產生（表示尚未被領養）
    - 若產生，一定晚於 open_date（至少 +1 天）
    """
    if pd.isna(open_date):
        return pd.NaT

    # 決定這隻動物有沒有被領養
    if random.random() > ADOPTION_RATE:
        return pd.NaT

    # 隨機在 opendate + 1 ~ MAX_DAYS_AFTER_OPEN 天內
    delta_days = random.randint(1, MAX_DAYS_AFTER_OPEN)
    return open_date + pd.Timedelta(days=delta_days)


def main():
    # 讀取原始 CSV
    # 如果你下載的是 UTF-8 with BOM，可以用 encoding="utf-8-sig"
    df = pd.read_csv(INPUT_CSV, encoding="utf-8")

    # 轉換 animal_opendate 成 datetime
    # 有些列可能為空字串，errors='coerce' 會變成 NaT
    if "animal_opendate" not in df.columns:
        raise ValueError("找不到欄位 'animal_opendate'，請確認 CSV 欄位名稱。")

    df["animal_opendate"] = pd.to_datetime(df["animal_opendate"], errors="coerce")

    # 新增被領養日欄位
    df["adoption_date"] = df["animal_opendate"].apply(gen_adoption_date)

    # 根據是否有被領養，決定哪些列要有領養人資訊
    adopted_mask = df["adoption_date"].notna()

    # 預先建立欄位，未被領養的先填 NaN
    df["adopter_name"] = np.nan
    df["adopter_phone"] = np.nan
    df["adopter_email"] = np.nan
    df["adopter_city"] = np.nan
    df["adopter_age"] = np.nan
    df["adopter_house_type"] = np.nan

    # 只對被領養的列填值
    adopted_indices = df.index[adopted_mask].tolist()

    for idx_i, row_idx in enumerate(adopted_indices):
        name = random.choice(ADOPTER_NAMES)
        df.at[row_idx, "adopter_name"] = name
        df.at[row_idx, "adopter_phone"] = random_phone()
        df.at[row_idx, "adopter_email"] = random_email(idx_i)
        df.at[row_idx, "adopter_city"] = random.choice(CITIES)
        df.at[row_idx, "adopter_age"] = random.randint(20, 65)
        df.at[row_idx, "adopter_house_type"] = random.choice(HOUSE_TYPES)

    # 驗證：所有有 adoption_date 的列都滿足 adoption_date > animal_opendate
    invalid_mask = adopted_mask & (df["adoption_date"] <= df["animal_opendate"])
    if invalid_mask.any():
        raise RuntimeError("有 adoption_date <= animal_opendate 的資料，邏輯錯誤。")

    # 輸出新的 CSV
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    print(f"已輸出到 {OUTPUT_CSV}，共 {len(df)} 筆，其中 {adopted_mask.sum()} 筆標記為已被領養。")


if __name__ == "__main__":
    main()
