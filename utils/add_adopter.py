import pandas as pd
import numpy as np
import random

# === 可調參數 ===
INPUT_CSV = "COA_OpenData.csv"                # 原始 CSV 檔名
OUTPUT_CSV = "COA_OpenData_with_adopter.csv"  # 輸出的 CSV 檔名
ADOPTION_RATE = 0.4                       # 有多少比例的動物被視為「已被領養」
MAX_DAYS_AFTER_OPEN = 60                  # 領養日會落在 opendate 之後 1 ~ 60 天

# 一些簡單的假資料池，可以自己改
def generate_random_name():
    """隨機產生中文姓名"""
    
    surnames = [
        "王", "陳", "張", "李", "林", "黃", "吳", "劉", "蔡", "楊",
        "許", "鄭", "謝", "郭", "洪", "邱", "曾", "廖", "賴", "徐",
        "周", "葉", "蘇", "莊", "呂", "江", "何", "蕭", "羅", "高",
        "潘", "朱", "簡", "鍾", "游", "詹", "胡", "施", "沈", "余",
        "盧", "梁", "趙", "顏", "柯", "翁", "魏", "孫", "戴",
        "姚", "方", "唐", "馮", "彭", "湯", "白", "田", "涂", "藍",
        "尤", "阮", "杜", "董", "程", "傅", "顧", "駱", "倪",
        "薛", "孟", "尹", "嚴", "韓", "喬", "金", "龔", "譚", "賀",
        "包", "康", "黎"
    ]

    
    given_names = [
        "明", "華", "文", "志", "美", "雅", "怡", "佳", "宜", "家",
        "建", "君", "智", "俊", "宏", "偉", "婷", "玲", "芳", "慧",
        "麗", "秀", "淑", "惠", "琴", "萍", "英", "菁", "瑜", "欣",
        "如", "安", "平", "祥", "豪", "強", "勇", "傑", "凱", "翔",
        "宇", "昌", "龍", "鳳", "春", "夏", "秋", "冬", "東", "南",
        "西", "北",
        "嘉", "榮", "德", "柏", "庭", "郁", "涵", "恩", "慈", "純",
        "潔", "臻", "柔", "萱", "筑", "筱", "瑋", "瑄", "瑤", "琬",
        "琪", "瑛", "詩", "晨", "暐", "昱", "泓", "澤", "宥", "宸",
        "承", "哲", "寬", "靖", "祺", "祐", "群", "彥", "逸", "樂",
        "倫", "哲", "淳", "涵", "遠", "諺", "柏", "靖"
    ]

    surname = random.choice(surnames)
    # 隨機決定名字是一個字還是兩個字
    if random.choice([True, False]):
        given_name = random.choice(given_names)
    else:
        given_name = random.choice(given_names) + random.choice(given_names)
    
    return surname + given_name

# ADOPTER_NAMES = [generate_random_name() for _ in range(500)]  # 產生50個隨機姓名池
CITIES = ["台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市", "基隆市", "新竹市", "嘉義市", "新竹縣", "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "屏東縣", "宜蘭縣", "花蓮縣", "台東縣", "澎湖縣", "金門縣", "連江縣"]
HOUSE_TYPES = ["公寓", "大樓華廈", "透天厝", "有庭院", "頂樓加蓋"]


def random_phone():
    # 台灣手機格式 09XXXXXXXX
    return "09" + "".join(str(random.randint(0, 9)) for _ in range(8))


def random_email(name_index: int):
    domains = ["gmail.com", "yahoo.com.tw", "yahoo.com", "hotmail.com", "outlook.com", "msa.hinet.net","cc.ncu.edu.tw"]
    english_names = ["james", "mary", "john", "patricia", "robert", "jennifer", "michael", "linda", "william", "elizabeth", "david", "barbara", "richard", "susan", "joseph", "jessica", "thomas", "sarah", "christopher", "karen", "charles", "nancy", "daniel", "lisa", "matthew", "betty", "anthony", "helen", "mark", "sandra", "donald", "donna", "steven", "carol", "paul", "ruth", "andrew", "sharon", "joshua", "michelle", "kenneth", "laura", "kevin", "sarah", "brian", "kimberly", "george", "deborah", "timothy", "dorothy"]
    
    name = random.choice(english_names)
    numbers = "".join(str(random.randint(0, 9)) for _ in range(random.randint(2, 4)))
    return f"{name_index}{name}{numbers}@{random.choice(domains)}"


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
    df["adopter_id"] = np.nan
    df["adopter_name"] = np.nan
    df["adopter_phone"] = np.nan
    df["adopter_email"] = np.nan
    df["adopter_city"] = np.nan
    df["adopter_age"] = np.nan
    df["adopter_house_type"] = np.nan

    # 只對被領養的列填值
    adopted_indices = df.index[adopted_mask].tolist()

    for idx_i, row_idx in enumerate(adopted_indices):
        # name = random.choice(ADOPTER_NAMES)
        name = generate_random_name()
        df.at[row_idx, "adopter_name"] = name
        df.at[row_idx, "adopter_phone"] = random_phone()
        df.at[row_idx, "adopter_email"] = random_email(idx_i)
        df.at[row_idx, "adopter_city"] = random.choice(CITIES)
        df.at[row_idx, "adopter_age"] = random.randint(20, 65)
        df.at[row_idx, "adopter_house_type"] = random.choice(HOUSE_TYPES)
        df.at[row_idx, "adopter_id"] = idx_i + 1  # 從 1 開始編號

    # 驗證：所有有 adoption_date 的列都滿足 adoption_date > animal_opendate
    invalid_mask = adopted_mask & (df["adoption_date"] <= df["animal_opendate"])
    if invalid_mask.any():
        raise RuntimeError("有 adoption_date <= animal_opendate 的資料，邏輯錯誤。")

    # 輸出新的 CSV
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    print(f"已輸出到 {OUTPUT_CSV}，共 {len(df)} 筆，其中 {adopted_mask.sum()} 筆標記為已被領養。")


if __name__ == "__main__":
    main()
