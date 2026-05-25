'''
練習題：電商商品銷售分析報表
主題:enumerate() + zip() + 商業分析邏輯
--------owo--------

妳現在是電商公司的資料分析助理。
公司有 5 個商品，本週記錄了：

1. 商品名稱
2. 銷售件數
3. 商品單價
4. 廣告花費

請使用 enumerate() 和 zip()，完成一份商品銷售分析報表。

已知資料：

products = ["藍牙耳機", "機械鍵盤", "無線滑鼠", "筆電支架", "USB-C 集線器"]

units_sold = [120, 45, 80, 30, 55]

unit_prices = [890, 2300, 650, 1200, 1500]

ad_costs = [18000, 25000, 9000, 8000, 12000]


題目要求：

1. 印出每個商品的銷售明細
   格式範例：
   1. 藍牙耳機|銷售件數:120 件|單價:890 元|廣告花費:18000 元

2. 計算每個商品的營收
   公式：
   營收 = 銷售件數 * 單價

3. 計算每個商品的 ROAS
   公式：
   ROAS = 營收 / 廣告花費

   ROAS 請顯示到小數點後兩位。

4. 根據 ROAS 判斷商品表現
   ROAS >= 5        → 表現優秀
   ROAS >= 3 且 < 5 → 表現普通
   ROAS < 3         → 表現偏弱

5. 計算全公司本週總營收

6. 找出本週營收最高的商品

7. 加分挑戰：
   找出「值得加碼廣告」的商品

   條件：
   ROAS >= 5 且 銷售件數 >= 50

   如果有符合條件的商品，輸出：
   建議加碼廣告：商品名稱

   如果沒有任何商品符合，輸出：
   目前沒有適合加碼廣告的商品

   輸出預期
=== 加碼廣告建議 ===
建議加碼廣告:商品A, 商品B

'''
# 商品名稱
products = ["藍牙耳機", "機械鍵盤", "無線滑鼠", "筆電支架", "USB-C 集線器"]

# 銷售件數
units_sold = [120, 45, 80, 30, 55]

# 商品單價
unit_prices = [890, 2300, 650, 1200, 1500]

# 廣告花費
ad_costs = [18000, 25000, 9000, 8000, 12000]

# 全公司本週總營收
weekly_total_revenue = 0

# 本週營收最高商品的營收
top_revenue_product = None
top_revenue_product_revenue = None

# 「值得加碼廣告」的商品
increase_ad_budget_products = []

# 印出每個商品的銷售明細
print()
print("=== 商品銷售明細 ===")
for number, (product, sold, price, ad_cost) in enumerate(zip(products, units_sold, unit_prices, ad_costs), start=1):

    print(f"{number}. {product}|銷售件數: {sold} 件|單價:{price} 元|廣告花費:{ad_cost} 元")

print()
print("=== 商品營收與 ROAS 分析 ===")
for number, (product, sold, price, ad_cost) in enumerate(zip(products, units_sold, unit_prices, ad_costs), start=1):
    revenue = sold * price
    product_roas = revenue / ad_cost
    weekly_total_revenue += revenue

    # 找週營收最高商品
    if top_revenue_product_revenue is None or top_revenue_product_revenue < revenue:
        top_revenue_product_revenue = revenue
        top_revenue_product = product

    # 根據 ROAS 判斷商品表現
    if product_roas >= 5:
        performance = "表現優秀"
    elif product_roas >= 3:
        performance = "表現普通"
    else:
        performance = "表現偏弱"

    # 印出商品營收與 ROAS 分析結果
    print(f"{number}.{product}|營收:{revenue} 元|ROAS:{product_roas:.2f} |表現: {performance}")

    # 判斷值得加碼廣告的商品
    if product_roas >= 5 and sold >= 50:
        increase_ad_budget_products.append(product)


print()
print("=== 總結報表 ===")
print(f"全公司本週總營收:{weekly_total_revenue} 元")
print(
    f"本週營收最高商品:{top_revenue_product}，營收: {top_revenue_product_revenue} 元")
print()
print("=== 加碼廣告建議 ===")
if increase_ad_budget_products:
    print(f"建議加碼廣告:{', '.join(increase_ad_budget_products)}")
else:
    print("目前沒有適合加碼廣告的商品")
