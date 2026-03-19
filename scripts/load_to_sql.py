import pandas as pd
import sqlite3

df = pd.read_csv("data/raw/transactions.csv", low_memory=False)

df = df.rename(columns={
    "TransactionID": "user_id",
    "TransactionAmt": "amount",
    "TransactionDT": "transaction_time",
    "isFraud": "is_fraud",
    "DeviceType": "device_id",
    "addr1": "location"
})

required_cols = [
    "user_id",
    "amount",
    "transaction_time",
    "is_fraud",
    "device_id",
    "location"
]
df = df[[c for c in required_cols if c in df.columns]]

df = df.dropna(subset=["user_id", "amount", "is_fraud"])

conn = sqlite3.connect("data/fraud.db")
df.to_sql("transactions", conn, if_exists="replace", index=False)
conn.close()

print("✅ IEEE dataset loaded into SQLite successfully")
