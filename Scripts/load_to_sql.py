import pandas as pd
from sqlalchemy import create_engine

# Load processed data
customers = pd.read_csv("data/processed/customers.csv")
products = pd.read_csv("data/processed/products.csv")
orders = pd.read_csv("data/processed/orders.csv")
sales = pd.read_csv("data/processed/sales.csv")

# Create connection
engine = create_engine("mysql+pymysql://root:Mysql%4008@localhost/sales_db")

# Load data into MySQL
customers.to_sql("customers", con=engine, if_exists="append", index=False)
products.to_sql("products", con=engine, if_exists="append", index=False)
orders.to_sql("orders", con=engine, if_exists="append", index=False)
sales.to_sql("sales", con=engine, if_exists="append", index=False)

print("Data loaded successfully")