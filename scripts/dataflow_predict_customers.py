import pandas as pd
import pickle
from src.components.transform_data import merge_dfs, create_bool_dummies, repl_na_bool, create_days2conversion, transform_cat_var

leads = pd.read_csv('./data/raw/olist_marketing_qualified_leads_dataset.csv', encoding='utf-8')
deals = pd.read_csv('./data/raw/olist_closed_deals_dataset.csv', encoding='utf-8')
marketing = merge_dfs(df_merge=[leads,deals], merge_var='mql_id', drop_vars=['sdr_id','sr_id'], na=['seller_id'])

marketing = create_bool_dummies(df=marketing, var_list=['declared_monthly_revenue', 'declared_product_catalog_size', 'average_stock'], rep_list=[0, 'unknown'])
marketing = repl_na_bool(df=marketing, var_list=['has_company','has_gtin'], value='false')
marketing = create_days2conversion(df= marketing, start='first_contact_date', end='won_date')
marketing = transform_cat_var(df=marketing, col_list=['origin', 'business_segment', 'lead_type', 'lead_behaviour_profile', 'has_company', 'has_gtin', 'business_type', 'bool_declared_monthly_revenue', 'bool_declared_product_catalog_size', 'bool_average_stock'])

feature_cols = ['origin', 'business_segment', 'lead_type', 'lead_behaviour_profile','has_company', 'has_gtin', 'business_type','bool_declared_monthly_revenue', 'bool_declared_product_catalog_size', 'bool_average_stock', 'days2conversion']
model = pickle.load(open('./data/model.pkl', 'rb'))
y_new = model.predict(marketing[feature_cols])

marketing['rfm_score'] = y_new
marketing.to_csv('./data/processed/scores_new_customers')