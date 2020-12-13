import pandas as pd
import pickle
from typing import List

from src.project.components.calc_scores import create_rfm_df
from src.general.utils import merge_dfs, transform_cat_var, create_bool_dummies, create_days2conversion, repl_na_bool
from src.project.components.train_classifier import train_classifier, get_reports

def flow_train(path:str, merge_df:List[pd.DataFrame], scores:pd.DataFrame) -> None:

    """Dataflow for training a new model as predictor for new customers scores based on past data.

    Parameters
    ----------
    path : str
        Path to directory where model will be saved after training

    merge_df : list[pd.DataFrame]
        Dataframes that need to be merged
    
    scores : pd.DataFrame
        Dataframe with RFM scores of existing sellers

    Returns
    -------
    [Print Output]
        Prints a classification report on the test data
    """    
    train = merge_dfs(df_merge=merge_df, merge_var='mql_id', drop_vars=['sdr_id','sr_id'], na=['seller_id'])
    train = merge_dfs(df_merge=[train, scores], merge_var='seller_id', drop_vars=['mql_id', 'landing_page_id', 'revenues', 'count_orders', 'days_last_activity', 'recency', 'frequency', 'monetary_ratio'], na=['rfm_score'])
    train = create_bool_dummies(df=train, var_list=['declared_monthly_revenue', 'declared_product_catalog_size', 'average_stock'], rep_list=[0, 'unknown'])
    train = repl_na_bool(df=train, var_list=['has_company','has_gtin'], value='false')
    train = create_days2conversion(df= train, start='first_contact_date', end='won_date')
    train = transform_cat_var(df=train, col_list=['origin', 'business_segment', 'lead_type', 'lead_behaviour_profile', 'has_company', 'has_gtin', 'business_type', 'bool_declared_monthly_revenue', 'bool_declared_product_catalog_size', 'bool_average_stock'])
    train = train.set_index(train.seller_id).drop(labels=['seller_id'], axis=1)
    feature_cols = ['origin', 'business_segment', 'lead_type', 'lead_behaviour_profile','has_company', 'has_gtin', 'business_type','bool_declared_monthly_revenue', 'bool_declared_product_catalog_size', 'bool_average_stock', 'days2conversion']
    model, X_test, y_test = train_classifier(train_data=train, feature_cols=feature_cols, target='rfm_score', test_size=0.1, cv=10, seed=42 )
    pickle.dump(model,open(path, 'wb'))

    return print(get_reports(model, X_test, y_test))

def flow_old(merge_df1:pd.DataFrame, merge_df2:pd.DataFrame, merge_df3:pd.DataFrame, key1:str, key2:str, rfm_range:int, rfm_vars:List[str]) -> pd.DataFrame:

    """Dataflow to calculate RFM scores for existing customers based on past data.

    Parameters
    ----------
    merge_df1 : pd.DataFrame
        Dataframe to be merged with merge_df2
    
    merge_df2: pd.DataFrame
        Dataframe to be merged with merge_df2
    
    merge_df3: pd.DataFrame
        Dataframe to be merged with joined merge_df1 and merge_df2

    key1 : str
        Key to merge merge_df1 and merge_df2

    key2 : str
        Key to merge third dataframe with previous joined dataframe of first and second dataframe in merge_df

    rfm_range : int
        Number of classes for RFM scores

    rfm_vars : list[str]
        List of variables needed to calculate the RFM scores

    Returns
    -------
    pd.DataFrame
        Dataframe with base information of existing customers and the calculated RFM scores
    """    
    commerce = merge_df1.merge(merge_df2, on=key1).merge(merge_df3, on=key2)
    rfm = create_rfm_df(orders_df=commerce, rfm_vars=rfm_vars, rfm_range=rfm_range)
    return rfm

def flow_new(new_customers:pd.DataFrame, model_path:str) -> pd.DataFrame:
    
    """Dataflow which predicts RFM score for new customers 

    Parameters
    ----------
    new_customers : pd.DataFrame
        Dataframes with all variables needed for predicting new RFM scores of new customers

    model_path : str
        Path to directory where model is saved

    Returns
    -------
    pd.DataFrame
        Dataframe with base information of new customers and the predicted RFM scores
    """    
    marketing = new_customers
    marketing = create_bool_dummies(df=marketing, var_list=['declared_monthly_revenue', 'declared_product_catalog_size', 'average_stock'], rep_list=[0, 'unknown'])
    marketing = repl_na_bool(df=marketing, var_list=['has_company','has_gtin'], value='false')
    marketing = create_days2conversion(df= marketing, start='first_contact_date', end='won_date')
    marketing = transform_cat_var(df=marketing, col_list=['origin', 'business_segment', 'lead_type', 'lead_behaviour_profile', 'has_company', 'has_gtin', 'business_type', 'bool_declared_monthly_revenue', 'bool_declared_product_catalog_size', 'bool_average_stock'])
    feature_cols = ['origin', 'business_segment', 'lead_type', 'lead_behaviour_profile','has_company', 'has_gtin', 'business_type','bool_declared_monthly_revenue', 'bool_declared_product_catalog_size', 'bool_average_stock', 'days2conversion']
    model = pickle.load(open(model_path, 'rb'))
    y_new = model.predict(marketing[feature_cols])
    marketing['rfm_score'] = y_new

    return marketing
