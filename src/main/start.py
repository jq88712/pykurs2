import argparse
import pandas as pd
import sys
sys.path.append('src/..')

from src.project.dataflows import flow_new, flow_old, flow_train

parser = argparse.ArgumentParser()
parser.add_argument('--customers_type', type=str, choices=['old','new'])
parser.add_argument('--train', type=str, choices=['yes', 'no'], default='no')
args = parser.parse_args()

leads = pd.read_csv('./data/raw/olist_marketing_qualified_leads_dataset.csv', encoding='utf-8')
deals = pd.read_csv('./data/raw/olist_closed_deals_dataset.csv', encoding='utf-8')
items = pd.read_csv('./data/raw/olist_order_items_dataset.csv', encoding='utf-8')
sellers = pd.read_csv('./data/raw/olist_sellers_dataset.csv', encoding='utf-8')
orders = pd.read_csv('./data/raw/olist_orders_dataset.csv', encoding='utf-8')

def main():
    if args.customers_type == 'old':
        #execute dataflow old customers
        scores = flow_old(merge_df=[orders, items, sellers], key1='order_id', key2='seller_id', rfm_range=5, rfm_vars=['seller_id', 'order_id', 'price', 'order_purchase_timestamp'])
        scores.to_csv('./data/processed/scores_historical_data.csv', encoding='utf-8')
        print('Scores for old customers created and exported to data folder')
    else:
        if args.train == 'yes':
            #execute dataflow old customers
            scores = flow_old(merge_df=[orders, items, sellers], key1='order_id', key2='seller_id', rfm_range=5, rfm_vars=['seller_id', 'order_id', 'price', 'order_purchase_timestamp'])
            #execute dataflow train
            flow_train(path='./data/model.pkl', merge_df=[leads, deals], scores=scores)
            #execute predict new customers
            new_scores = flow_new(merge_df=[leads, deals], model_path='./data/model.pkl')
            new_scores.to_csv('./data/processed/scores_new_customers.csv', encoding='utf-8')
            print('Scores for new customers created and exported to data folder')

        else: 
            #execute dataflow predict new customers
            new_scores = flow_new(merge_df=[leads, deals], model_path='./data/model.pkl')
            new_scores.to_csv('./data/processed/scores_new_customers.csv', encoding='utf-8')
            print('Scores for new customers created and exported to data folder')

if __name__ == "__main__":
    print('Scores are calculated ...')
    main()
