from sklearn.linear_model import LogisticRegressionCV
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_classifier(df:pd.DataFrame, feature_cols:list[str], target:str, test_size:float, cv:int, seed:int) -> tuple[LogisticRegressionCV, list, list]:
    X = df[feature_cols]
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=test_size, random_state=seed)
    classifier = LogisticRegressionCV(cv=cv, solver='sag', random_state=seed, n_jobs=-1)
    model = classifier.fit(X_train, y_train)
    return model, X_test, y_test

#TODO: get_reports scheint immer mit train_classifier aufzutauchen - warum kein object hier?, dann kann man die objecte halten.

def get_reports(model:LogisticRegressionCV, X_test:list, y_test:list) -> None:
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))