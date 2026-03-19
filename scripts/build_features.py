import pandas as pd
import sqlite3

# Connect to SQLite
conn = sqlite3.connect("data/fraud.db")

# Run SQL aggregation
query = open("sql/features.sql").read()
features = pd.read_sql_query(query, conn)

# Compute standard deviation in pandas
amount_df = pd.read_sql_query(
    "SELECT user_id, amount FROM transactions", conn
)

std_amount = (
    amount_df.groupby("user_id")["amount"]
    .std()
    .fillna(0)
    .reset_index()
    .rename(columns={"amount": "std_amount"})
)

# Merge std feature
features = features.merge(std_amount, on="user_id", how="left")

# Save feature table
features.to_csv("data/processed/fraud_features.csv", index=False)

conn.close()

print("✅ Feature table created successfully")
