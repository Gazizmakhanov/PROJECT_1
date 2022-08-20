import pandas as pd
import numpy as np
from scipy import stats
import env
import os

import env

def get_connection(db, user=env.username, host=env.database, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def get_titanic_data():
    filename='titanic.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df= pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        df.to_csv(filename)
        return df


def get_iris_data():
    filename='iris.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df= pd.read_sql('''SELECT * FROM measurements
JOIN species
USING (species_id)''', get_connection('iris_db'))
        df.to_csv(filename)
        return df

def get_telco_data():
    filename='telco.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df= pd.read_sql('''select * 
                        from customer_contracts
                        join customers using(customer_id)
                        join internet_service_types using(internet_service_type_id)
                        join payment_types using(payment_type_id)''', get_connection('telco_churn'))
        df.to_csv(filename)
        return df
    



