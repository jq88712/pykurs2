import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

#TODO: "transform_data" ist sehr generisch

def merge_dfs(df_merge:list, merge_var:str, drop_vars:list, na:list) -> pd.DataFrame:
    df = pd.merge(df_merge[0], df_merge[1], on=merge_var, how='left')
    df = df.drop(drop_vars, axis=1)
    df = df.dropna(subset=na)
    return df

#TODO: Name "df" ist nicht gerade gut
def create_bool_dummies(df:pd.DataFrame, var_list:list, rep_list:list) -> pd.DataFrame:
    for var in var_list:
        df[var] = df[var].replace(to_replace=rep_list ,value= np.nan)
        df['bool_'+var] = ['False' if pd.isna(x) == True else 'True' for x in df[var]]
        df = df.drop(var, axis=1)
    return df

def repl_na_bool(df: pd.DataFrame, var_list:list, value:str) -> pd.DataFrame:
    for var in var_list:
        df[var] = df[var].replace(to_replace= [np.nan], value= value)
    return df

def create_days2conversion(df:pd.DataFrame, start:pd.Series, end:pd.Series) -> pd.DataFrame:
    df[start] = pd.to_datetime(df[start]).dt.date.astype('datetime64')
    df[end] = pd.to_datetime(df[end]).dt.date.astype('datetime64')
    df['days2conversion'] = (df[end] - df[start]).dt.days
    df = df.drop([start,end], axis=1)
    return df

def transform_cat_var(df:pd.DataFrame, col_list:list) -> pd.DataFrame:
    for col in col_list:
        df[col] = df[col].astype(str)
        df[col] = LabelEncoder().fit_transform(df[col])
    return df