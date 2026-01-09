import pandas as pd
import random
from faker import Faker
from sqlalchemy import create_engine
from textblob import TextBlob
from datetime import datetime, timedelta

# 1. Setup the Database Connection (Creates a file named 'trendpulse.db')
db_engine = create_engine('sqlite:///trendpulse.db')
fake = Faker()

print("🚀 Initializing TrendPulse Database...")

# --- DATA GENERATION FUNCTIONS ---

def generate_products():
    """Create a list of fictional products"""
    products = [
        {'product_id': 101, 'product_name': 'Neon X-1 (Sneakers)', 'category': 'Footwear', 'price': 120},
        {'product_id': 102, 'product_name': 'Eco-Hoodie', 'category': 'Apparel', 'price': 65},
        {'product_id': 103, 'product_name': 'SmartWatch Z', 'category': 'Electronics', 'price': 250},
        {'product_id': 104, 'product_name': 'Retro Cap', 'category': 'Accessories', 'price': 25},
    ]
    return pd.DataFrame(products)

def generate_sales(products_df, num_records=500):
    """Generate fake sales transactions linked to products"""
    sales_data = []
    start_date = datetime.now() - timedelta(days=30) # Past 30 days
    
    for _ in range(num_records):
        prod = products_df.sample(1).iloc[0]
        date = fake.date_time_between(start_date=start_date, end_date='now')
        
        # Simulating logic: Weekend sales are slightly higher
        qty = random.randint(1, 3)
        
        sales_data.append({
            'transaction_id': fake.uuid4(),
            'date': date,
            'product_id': prod['product_id'],
            'quantity': qty,
            'total_revenue': qty * prod['price']
        })
    return pd.DataFrame(sales_data)

def generate_social_media(num_posts=300):
    """Generate fake social media posts and analyze sentiment"""
    platforms = ['Twitter', 'Instagram', 'Reddit']
    posts = []
    start_date = datetime.now() - timedelta(days=30)
    
    # Pre-defined templates to simulate 'Trends'
    positive_templates = ["Love the new {product}!", "Amazing quality on the {product}.", "Best purchase ever!", "TrendPulse brand is killing it!"]
    negative_templates = ["Hate the delivery time for {product}.", "The {product} broke in two days.", "Waste of money.", "Customer service is bad."]
    
    products_list = ['Neon X-1', 'Eco-Hoodie', 'SmartWatch Z']
    
    for _ in range(num_posts):
        date = fake.date_time_between(start_date=start_date, end_date='now')
        platform = random.choice(platforms)
        
        # Randomly decide if this post is happy or angry
        if random.random() > 0.3: # 70% chance of positive
            template = random.choice(positive_templates)
        else:
            template = random.choice(negative_templates)
            
        text = template.format(product=random.choice(products_list))
        
        # --- AI PART: SENTIMENT ANALYSIS ---
        # We use TextBlob to calculate polarity (-1 to 1)
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        
        posts.append({
            'post_id': fake.uuid4(),
            'date': date,
            'platform': platform,
            'content': text,
            'sentiment_score': sentiment_score # The AI Score
        })
        
    return pd.DataFrame(posts)

# --- EXECUTION ---

# 1. Generate Dataframes
df_products = generate_products()
df_sales = generate_sales(df_products)
df_social = generate_social_media()

# 2. Upload to SQL Database
# 'if_exists="replace"' means it will overwrite the table if we run this script again
df_products.to_sql('products', db_engine, index=False, if_exists='replace')
df_sales.to_sql('sales', db_engine, index=False, if_exists='replace')
df_social.to_sql('social_buzz', db_engine, index=False, if_exists='replace')

print("✅ SUCCESS! Database 'trendpulse.db' created.")
print(f"📊 Products: {len(df_products)} rows")
print(f"💰 Sales Transactions: {len(df_sales)} rows")
print(f"🐦 Social Media Posts: {len(df_social)} rows")