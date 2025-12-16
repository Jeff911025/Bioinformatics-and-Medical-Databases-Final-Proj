import os
import sqlite3

def create_clean_db(db_path="test.db"):
    # 如果已存在，先刪除
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Removed old database: {db_path}")

    # 建立新的空資料庫
    conn = sqlite3.connect(db_path)
    conn.close()

    print(f"Created clean database: {db_path}")
    
if __name__ == "__main__":
    create_clean_db()