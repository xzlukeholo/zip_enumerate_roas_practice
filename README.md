# 🛒 電商商品銷售分析報表 (E-commerce Product Sales Analysis Report)

這是一個基於 Python 核心語法實現的電商資料分析練習專案。本專案模擬電商公司的資料分析助理，透過處理商品銷售、單價與廣告花費等數據，自動生成商品銷售明細、營收計算、廣告投資報酬率 (ROAS) 評估以及公司整週的業績總結報表。

This is a Python-based e-commerce data analysis practice project. Simulating the role of a data analyst assistant, this script processes weekly sales data, unit prices, and ad spending to automatically generate comprehensive sales reports, revenue calculations, ROAS evaluations, and a weekly business summary.

---

## 💡 核心技術與語法 (Key Features)

本專案的第一版核心在於展示 Python 內建迭代工具的高效搭配：
The first version of this project demonstrates the efficient combination of Python's built-in iteration tools:

- **`zip()` 多序列並行處理**：將商品名稱、銷售件數、單價、廣告花費等多個一維列表（Lists）打包成單一迭代器，確保資料對齊。
- **`enumerate(..., start=1)` 索引追蹤**：在遍歷資料的同時，優雅地自動生成符合商業報表習慣的商品編號（從 1 開始）。
- **多變數解包 (Unpacking)**：在 `for` 迴圈中直接將 `zip` 打包的元組（Tuple）解包至對應變數，提升程式碼可讀性。
- **商務邏輯計算 (Business Logic)**：
  - **營收 (Revenue)** = 銷售件數 $\times$ 單價
  - **ROAS (Return on Ad Spend)** = 營收 $/$ 廣告花費（使用 f-string `:.2f` 格式化輸出至小數點後兩位）。
  - **績效動態評級**：依據 ROAS 水平自動歸類商品表現（表現優秀 / 普通 / 偏弱）。

---

## 數據源 (Data Source)

專案內置模擬的 5 項熱銷電子產品本週數據：
The script analyzes the following mock dataset for 5 electronics products:

| 商品名稱 (Product) | 銷售件數 (Units Sold) | 商品單價 (Unit Price) | 廣告花費 (Ad Cost) |
| :--- | :---: | :---: | :---: |
| 藍牙耳機 | 120 | $890 | $18,000 |
| 機械鍵盤 | 45 | $2,300 | $25,000 |
| 無線滑鼠 | 80 | $650 | $9,000 |
| 筆電支架 | 30 | $1,200 | $8,000 |
| USB-C 集線器 | 55 | $1,500 | $12,000 |

---

## 📈 執行結果範例 (Output Example)

運行 `analysis.py` 後將在終端機輸出以下標準報表：

```text
=== 商品銷售明細 ===
1. 藍牙耳機|銷售件數: 120 件|單價:890 元|廣告花費:18000 元
2. 機械鍵盤|銷售件數: 45 件|單價:2300 元|廣告花費:25000 元
...

=== 商品營收與 ROAS 分析 ===
1.藍牙耳機|營收:106800 元|ROAS:5.93 |表現: 表現優秀
2.機械鍵盤|營收:103500 元|ROAS:4.14 |表現: 表現普通
...

=== 總結報表 ===
全公司本週總營收:416300 元
本週營收最高商品:藍牙耳機，營收: 106800 元

🛠️ 未來優化方向 (Future Improvements / TODO)
效能優化 (Performance)：目前版本使用雙迴圈分別處理明細與分析，下一版預計將迴圈合併為單次遍歷，降低時間複雜度。

結構重構 (Refactoring)：優化最高營收商品的追蹤邏輯，直接儲存商品字串，減少索引轉換的潛在錯誤。