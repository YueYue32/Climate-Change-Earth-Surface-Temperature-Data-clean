# ===============================
# 檔案名稱: climate_data_processing.py
# 功能: 清理氣候資料並計算城市平均溫度
# ===============================

import pandas as pd

def load_data(file_path):
    """
    讀取 CSV 檔案
    """
    df = pd.read_csv(file_path)
    print(f"資料載入完成，總列數: {len(df)}")
    return df

def clean_data(df):
    """
    資料清理流程：
    1. 處理缺失值
    2. 去除重複資料
    """
    # 缺失值填補：以城市平均值填補
    df['AverageTemperature'] = df.groupby('City')['AverageTemperature'].transform(
        lambda x: x.fillna(x.mean())
    )
    df['AverageTemperatureUncertainty'] = df.groupby('City')['AverageTemperatureUncertainty'].transform(
        lambda x: x.fillna(x.mean())
    )

    # 若仍有缺失值，刪除
    df.dropna(inplace=True)

    # 去除重複資料
    df.drop_duplicates(inplace=True)

    print("資料清理完成")
    return df

def calculate_city_year_avg(df):
    """
    計算每個城市每年的平均溫度
    """
    # 將 dt 轉成年份
    df['Year'] = pd.to_datetime(df['dt']).dt.year

    # 計算每個城市每年的平均溫度
    city_year_avg = df.groupby(['City', 'Year'])['AverageTemperature'].mean().reset_index()

    print("城市年度平均溫度計算完成")
    return city_year_avg

def save_data(df_cleaned, city_year_avg, cleaned_file, city_avg_file):
    """
    儲存清理後資料及城市年度平均溫度
    """
    df_cleaned.to_csv(cleaned_file, index=False)
    city_year_avg.to_csv(city_avg_file, index=False)
    print(f"清理後資料已儲存: {cleaned_file}")
    print(f"城市年度平均溫度已儲存: {city_avg_file}")

def main():
    # CSV 路徑
    input_file = "C:/Users/user/Desktop/資料工程專案設計/recent_20years.csv"
    cleaned_file = "C:/Users/user/Desktop/資料工程專案設計/cleaned_recent_20years.csv"
    city_avg_file = "C:/Users/user/Desktop/資料工程專案設計/city_year_avg.csv"

    # 讀取資料
    df = load_data(input_file)

    # 資料清理
    df_cleaned = clean_data(df)

    # 計算城市年度平均溫度
    city_year_avg = calculate_city_year_avg(df_cleaned)

    # 儲存資料
    save_data(df_cleaned, city_year_avg, cleaned_file, city_avg_file)

if __name__ == "__main__":
    main()
