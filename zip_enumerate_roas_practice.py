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

# 3. 計算每個商品的 ROAS
#    公式：
#    ROAS = 營收 / 廣告花費

#    ROAS 請顯示到小數點後兩位。

# 4. 根據 ROAS 判斷商品表現
#    ROAS >= 5        → 表現優秀
#    ROAS >= 3 且 < 5 → 表現普通
#    ROAS < 3         → 表現偏弱

5. 計算全公司本週總營收

6. 找出本週營收最高的商品

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

# 本週營收最高商品價格
top_revenue_product_revenue = 0

# 印出每個商品的銷售明細
print()
print("=== 商品銷售明細 ===")
for number, (product, sold, price, cost) in enumerate(zip(products, units_sold, unit_prices, ad_costs), start=1):

    print(f"{number}. {product}|銷售件數: {sold} 件|單價:{price} 元|廣告花費:{cost} 元")

print()
print("=== 商品營收與 ROAS 分析 ===")
for number, (product, sold, price, cost) in enumerate(zip(products, units_sold, unit_prices, ad_costs), start=1):
    revenue = sold * price
    product_roas = revenue / cost
    weekly_total_revenue += revenue

    # 找週營收最高商品
    if top_revenue_product_revenue < revenue:
        top_revenue_product_revenue = revenue
        top_revenue_product = product

    if product_roas >= 5:
        print(f"{number}.{product}|營收:{revenue} 元|ROAS:{product_roas:.2f} |表現: 表現優秀")
    elif product_roas >= 3:
        print(f"{number}.{product}|營收:{revenue} 元|ROAS:{product_roas:.2f} |表現: 表現普通")
    elif product_roas < 3:
        print(f"{number}.{product}|營收:{revenue} 元|ROAS:{product_roas:.2f} |表現: 表現偏弱")

print()
print("=== 總結報表 ===")
print(f"全公司本週總營收:{weekly_total_revenue} 元")
print(
    f"本週營收最高商品:{top_revenue_product}，營收: {top_revenue_product_revenue} 元")
