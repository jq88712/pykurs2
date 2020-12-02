import pandas as pd
import pickle
from src.components.transform_data import *
from src.components.train_classifier import *
from src.components.calc_scores import *

leads = pd.read_csv('../data/raw/olist_marketing_qualified_leads_dataset.csv', encoding='utf-8')
deals = pd.read_csv('../data/raw/olist_closed_deals_dataset.csv', encoding='utf-8')
items = pd.read_csv('../data/raw/olist_order_items_dataset.csv', encoding='utf-8')
sellers = pd.read_csv('../data/raw/olist_sellers_dataset.csv', encoding='utf-8')
orders = pd.read_csv('../data/raw/olist_orders_dataset.csv', encoding='utf-8')

commerce = pd.merge(orders, items, on='order_id')
commerce = commerce.merge(sellers, on='seller_id')
rfm = create_rfm_df(sellers=commerce.seller_id, orders=commerce.order_id, prices=commerce.price, time=commerce.order_purchase_timestamp, rfm_range=5)

marketing = merge_dfs(df_merge=[leads,deals], merge_var='mql_id', drop_vars=['sdr_id','sr_id'], na=['seller_id'])
train = marketing.copy()

train = merge_dfs(df_merge=[train, rfm], merge_var='seller_id', drop_vars=['mql_id', 'landing_page_id', 'revenues', 'count_orders', 'days_last_activity', 'recency', 'frequency', 'monetary_ratio'], na=['rfm_score'])
train = create_bool_dummies(df=train, var_list=['declared_monthly_revenue', 'declared_product_catalog_size', 'average_stock'], rep_list=[0, 'unknown'])
train = repl_na_bool(df=train, var_list=['has_company','has_gtin'], value='false')
train = create_days2conversion(df= train, start='first_contact_date', end='won_date')
train = transform_cat_var(df=train, col_list=['origin', 'business_segment', 'lead_type', 'lead_behaviour_profile', 'has_company', 'has_gtin', 'business_type', 'bool_declared_monthly_revenue', 'bool_declared_product_catalog_size', 'bool_average_stock'])
train = train.set_index(train.seller_id).drop(labels=['seller_id'], axis=1)

feature_cols = ['origin', 'business_segment', 'lead_type', 'lead_behaviour_profile','has_company', 'has_gtin', 'business_type','bool_declared_monthly_revenue', 'bool_declared_product_catalog_size', 'bool_average_stock', 'days2conversion']
model, X_test, y_test = train_classifier(df=train, feature_cols=feature_cols, target='rfm_score', test_size=0.1, cv=10, seed=42 )
get_reports(model, X_test, y_test)

pickle.dump(model,open('./data/model.pkl', 'wb'))