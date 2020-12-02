import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def merge_dfs(df_merge, merge_var, drop_vars, na):
    df = pd.merge(df_merge[0], df_merge[1], on=merge_var, how='left')
    df = df.drop(drop_vars, axis=1)
    df = df.dropna(subset=na)
    return df

def create_bool_dummies(df, var_list, rep_list):
    for var in var_list:
        df[var] = df[var].replace(to_replace=rep_list ,value= np.nan)
        df['bool_'+var] = ['False' if pd.isna(x) == True else 'True' for x in df[var]]
        df = df.drop(var, axis=1)
    return df

def repl_na_bool(df, var_list, value):
    for var in var_list:
        df[var] = df[var].replace(to_replace= [np.nan], value= value)
    return df

def create_days2conversion(df, start, end):
    df[start] = pd.to_datetime(df[start]).dt.date.astype('datetime64')
    df[end] = pd.to_datetime(df[end]).dt.date.astype('datetime64')
    df['days2conversion'] = (df[end] - df[start]).dt.days
    df = df.drop([start,end], axis=1)
    return df

def transform_cat_var(df, col_list):
    for col in col_list:
        df[col] = df[col].astype(str)
        df[col] = LabelEncoder().fit_transform(df[col])
    return df