import pandas as pd
import sqlalchemy

# 1. Connect to our existing database
engine = sqlalchemy.create_engine('sqlite:///trendpulse.db')

print("⏳ Extracting data for Power BI...")

# 2. Read the tables
df_sales = pd.read_sql("SELECT * FROM sales", engine)
df_social = pd.read_sql("SELECT * FROM social_buzz", engine)

# 3. Export to CSV (Power BI loves CSVs)
df_sales.to_csv("powerbi_sales.csv", index=False)
df_social.to_csv("powerbi_social.csv", index=False)

print("✅ Data exported! Open Power BI and load 'powerbi_sales.csv' and 'powerbi_social.csv'.")