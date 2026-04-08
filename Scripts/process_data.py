import pandas as pd

df = pd.read_csv("data/raw/sales.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
print("Rows before cleaning :", len(df))
df.drop_duplicates(inplace=True)
df.dropna(subset=['customer_id', 'product_id', 'order_id', 'sales', 'quantity'], inplace=True)

df = df[(df['sales'] > 0) & (df['quantity'] > 0)]


customers = df[['customer_id','customer_name','segment','region']].drop_duplicates()

products = df[['product_id','product_name','category','sub_category']].drop_duplicates()

orders = df[['order_id','order_date','ship_date','ship_mode','customer_id']].drop_duplicates()

sales = df[['order_id','product_id','sales','quantity','discount','profit']].drop_duplicates()

orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
orders['ship_date'] = pd.to_datetime(orders['ship_date'], errors='coerce')
orders.dropna(subset=['order_date', 'ship_date'], inplace=True)


customers.to_csv("data/processed/customers.csv", index=False)
products.to_csv("data/processed/products.csv", index=False)
orders.to_csv("data/processed/orders.csv", index=False)
sales.to_csv("data/processed/sales.csv", index=False)


print("Rows after cleaning :", len(df))
print(df.isnull().sum())