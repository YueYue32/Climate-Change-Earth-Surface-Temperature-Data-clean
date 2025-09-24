# Climate-Change-Earth-Surface-Temperature-Data-clean
# Climate Data Processing Project
全球地表溫度的歷史數據_資料整理(use pandas)


## 專案簡介
這是一個針對全球氣候資料的資料工程專案，使用 Python 與 pandas 完成資料清理與處理。專案流程包含：
1. 篩選出近 20 年資料
2. 缺失值處理
3. 重複資料清理
4. 計算城市每年的平均溫度
5. 將處理後資料儲存成新 CSV 檔案，方便後續分析或視覺化

資料來源：使用 Kaggle 的 [Climate Change: Earth Surface Temperature Data](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)

---

## 專案結構
```

climate_data_project/

│
├── recent_20years.csv # 篩選近20年的原始資料
├── processed_climate_data.csv # 清理後並加入城市年度平均溫度的新資料
├── climate_data_processing.py # 資料清理與處理程式
└── README.md # 專案說明
```

---


**功能說明**
1. 缺失值處理
AverageTemperature 、 AverageTemperatureUncertainty 欄位若缺失，會以該城市的平均值填補
若仍有缺失值，會刪除該筆資料<br>

2. 重複資料清理<br>
對整筆資料去除完全重複的列<br>

3. 城市年度平均溫度
計算每個城市每年的平均溫度，並加入原始資料作為新欄位 AvgTempPerYear

4. 最終資料輸出
輸出 CSV：processed_climate_data.csv


新檔案包含原始資料與城市年度平均溫度，可直接進行後續分析或視覺化
