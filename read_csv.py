import pandas as pd
from datetime import datetime

# 讀取 CSV
df = pd.read_csv("C:/Users/user/Desktop/資料工程專案設計/GlobalLandTemperaturesByCity.csv")

# 將 dt 欄位轉成 datetime 型態
df['dt'] = pd.to_datetime(df['dt'], format='%Y-%m-%d', errors='coerce')

# 設定時間範圍：近50年
current_year = datetime.now().year
start_year = current_year - 20

# 篩選資料
df_recent = df[df['dt'].dt.year >= start_year]

# 儲存成新 CSV
df_recent.to_csv("C:/Users/user/Desktop/資料工程專案設計/recent_20years.csv", index=False)

