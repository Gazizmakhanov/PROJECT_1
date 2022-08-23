import pandas as pd
import numpy as np
from scipy import stats
import env
import os

import env

def get_connection(db, user=env.username, host=env.database, password=env.password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def get_titanic_data():
    '''
    This function reads in titanic data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    filename='titanic.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df= pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))
        df.to_csv(filename)
        return df


def get_iris_data():
    '''
    This function reads in iris data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
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
    '''
    This function reads in telco data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    filename='telco.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df= pd.read_sql('''select * 
                        from customer_contracts
                        join customers using(customer_id)
                        join internet_service_types using(internet_service_type_id)
                        join payment_types using(payment_type_id)''', get_connection('telco_churn'))
       
        return df 
    



