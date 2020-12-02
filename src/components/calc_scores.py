import pandas as pd

def calc_recency(sellers, time):
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

def calc_frequency(sellers: pd.Series):
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

def calc_monetary(orders, prices, sellers):
    frame = {'orders':orders, 'prices': prices, 'sellers': sellers}
    df = pd.DataFrame(frame)
    orders_revenues = df.groupby(by='orders').sum()
    df = df.merge(orders_revenues,on='orders')
    seller_revenues = df.groupby(by='sellers').sum().round(2)
    
    return  dict(zip(seller_revenues.index,seller_revenues.prices_y))

def create_rfm_df(sellers, orders, prices, time, rfm_range) -> pd.DataFrame:
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