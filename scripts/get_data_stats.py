import pandas as pd 

def get_basic_stats(df):
    a = df.head(5)
    b = df.info()
    return print(a,b)

def get_barh_var(variable, figsize, ascending):
    counts = variable.value_counts().sort_index(ascending=False).sort_values(ascending=False)
    plot = counts.head(10).sort_values(ascending=ascending).plot.barh(figsize=figsize)
    return print(plot)

leads = pd.read_csv('./data/raw/olist_marketing_qualified_leads_dataset.csv', encoding='utf-8')
get_basic_stats(leads)
get_barh_var(leads.origin, figsize=[10,5], ascending=True)