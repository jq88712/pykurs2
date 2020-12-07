import pandas as pd

def calc_recency(sellers:pd.Series, time:pd.Series) -> dict:
    latest = max(pd.to_datetime(time).dt.date)
    start = min(pd.to_datetime(time).dt.date)
    recency = {}

    for seller, time in zip(sellers, pd.to_datetime(time).dt.date):
        if seller in recency:
            if time > recency[seller]:
                recency[seller] = time
            else:
                recency[seller] = recency[seller]
        else:
            recency[seller] = start

    for key in recency:
        recency[key] = (latest - recency[key]).days
    
    return recency

def calc_frequency(sellers:pd.Series) -> dict:
    unique_sellers = sellers.unique()
    counts = []

    for seller in unique_sellers:
        counter = 0
        for row in sellers:
            if row == seller:
                counter += 1
            else:
                counter = counter
        counts.append(counter)

    return dict(zip(unique_sellers,counts))

def calc_monetary(orders:pd.Series, prices:pd.Series, sellers:pd.Series) -> dict:
    frame = {'orders':orders, 'prices': prices, 'sellers': sellers}
    df = pd.DataFrame(frame)
    orders_revenues = df.groupby(by='orders').sum()
    df = df.merge(orders_revenues,on='orders')
    seller_revenues = df.groupby(by='sellers').sum().round(2)
    
    return  dict(zip(seller_revenues.index,seller_revenues.prices_y))

#TODO: def create_rfm_df(commerce, rfm_vars, rfm_range:int) -> pd.DataFrame:
def create_rfm_df(sellers:pd.Series, orders:pd.Series, prices:pd.Series, time:pd.Series, rfm_range:int) -> pd.DataFrame:
    
    """Function which calculate the RFM score of each customer by calculation each R/F/M dimension to divide into classes. Lastly the mean is calculated of each seller over the 3 dimensions.

    Parameters
    ----------
    sellers : pd.Series
        Variable containing seller ids
    
    orders : pd.Series
        Variable containing order ids

    prices : pd.Series
        Variable containing item prices

    time : pd.Series
        Variable containing order time stamps

    rfm_range : int
        Number of classes for scores
    
    Returns
    -------
    pd.DataFrame
        Dataframe with sellers, calculated base information, R/F/M scores and RFM score
    """
	#TODO:
    # sellers=commerce[rfm_vars[0]]
    # orders=commerce[rfm_vars[1]]
    # prices=commerce[rfm_vars[2]]
    # time=commerce[rfm_vars[3]]

    labels = range(1, (rfm_range+1))
    scores = pd.DataFrame()
    scores['seller_id'] = sellers.unique()
    scores['revenues'] = scores.seller_id.map(calc_monetary(orders, prices, sellers))
    scores['count_orders'] = scores.seller_id.map(calc_frequency(sellers))
    scores['days_last_activity'] = scores.seller_id.map(calc_recency(sellers, time))
    scores['recency'] = pd.qcut(scores.days_last_activity,q=rfm_range, labels=labels)
    scores['frequency'] = pd.qcut(scores.count_orders,q=rfm_range, labels=labels)
    scores['monetary_ratio'] = pd.qcut(scores.revenues,q=rfm_range, labels=labels)
    scores['rfm_score'] = scores[['recency','frequency', 'monetary_ratio']].mean(axis=1).round(0)
    return scores  