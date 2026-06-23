import pandas as pd
import sqlite3

# Load Excel dataset
df = pd.read_excel(r"C:\week2Decode\week1\Cleaned_Dataset.xlsx")

# Create SQLite database
conn = sqlite3.connect("orders.db")

# Store data in SQL table
df.to_sql("orders", conn, if_exists="replace", index=False)

cursor = conn.cursor()

print("\n===== TOTAL ORDERS =====")
cursor.execute("""
SELECT COUNT(*) AS Total_Orders
FROM orders;
""")
print(cursor.fetchall())

print("\n===== AVERAGE ORDER VALUE =====")
cursor.execute("""
SELECT AVG(TotalPrice) AS Average_Order_Value
FROM orders;
""")
print(cursor.fetchall())

print("\n===== TOTAL REVENUE =====")
cursor.execute("""
SELECT SUM(TotalPrice) AS Total_Revenue
FROM orders;
""")
print(cursor.fetchall())

print("\n===== ORDERS BY PRODUCT =====")
cursor.execute("""
SELECT Product,
       COUNT(*) AS Order_Count
FROM orders
GROUP BY Product
ORDER BY Order_Count DESC;
""")
for row in cursor.fetchall():
    print(row)

print("\n===== REVENUE BY PRODUCT =====")
cursor.execute("""
SELECT Product,
       SUM(TotalPrice) AS Revenue
FROM orders
GROUP BY Product
ORDER BY Revenue DESC;
""")
for row in cursor.fetchall():
    print(row)

print("\n===== ORDERS BY PAYMENT METHOD =====")
cursor.execute("""
SELECT PaymentMethod,
       COUNT(*) AS Total_Orders
FROM orders
GROUP BY PaymentMethod;
""")
for row in cursor.fetchall():
    print(row)

print("\n===== DELIVERED ORDERS =====")
cursor.execute("""
SELECT *
FROM orders
WHERE OrderStatus='Delivered'
LIMIT 10;
""")
for row in cursor.fetchall():
    print(row)

print("\n===== TOP 10 HIGHEST VALUE ORDERS =====")
cursor.execute("""
SELECT OrderID, Product, TotalPrice
FROM orders
ORDER BY TotalPrice DESC
LIMIT 10;
""")
for row in cursor.fetchall():
    print(row)

print("\n===== AVERAGE QUANTITY BY PRODUCT =====")
cursor.execute("""
SELECT Product,
       AVG(Quantity) AS Avg_Quantity
FROM orders
GROUP BY Product;
""")
for row in cursor.fetchall():
    print(row)

conn.close()

print("\nProject 3 SQL Analysis Completed Successfully!")