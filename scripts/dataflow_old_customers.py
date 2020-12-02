import pandas as pd
from src.components.calc_scores import create_rfm_df

items = pd.read_csv('../data/raw/olist_order_items_dataset.csv', encoding='utf-8')
sellers = pd.read_csv('../data/raw/olist_sellers_dataset.csv', encoding='utf-8')
orders = pd.read_csv('../data/raw/olist_orders_dataset.csv', encoding='utf-8')

commerce = pd.merge(orders, items, on='order_id')
commerce = commerce.merge(sellers, on='seller_id')
rfm = create_rfm_df(sellers=commerce.seller_id, orders=commerce.order_id, prices=commerce.price, time=commerce.order_purchase_timestamp, rfm_range=5)
rfm.to_csv('../data/processed/scores_historical_data.csv', encoding='utf-8')