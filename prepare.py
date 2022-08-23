import pandas as pd
import numpy as np

# import splitting functions
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer


def prep_iris(iris):
    '''
    This function takes in the iris data acquired by get_iris_data,
    dropes unnececary columns and renames column species_name to species.
    returns cleaned up ready to explore data.
    '''
    iris = iris.drop(columns=['species_id','measurement_id'])
    iris = iris.rename(columns={'species_name':'species'})
    dummy_iris = pd.get_dummies(iris.species, drop_first=True)
    iris = pd.concat([iris, dummy_iris], axis=1)
    return iris


def prep_titanic(titanic):
    '''
    This function takes in the titanic data acquired by get_titanic_data,
   dropes unnececary columns. Filles up missing values, creates and concats dummies
   returns cleaned up ready to explore data.
   
    '''
    titanic = titanic.drop(columns=['embarked','class','deck'])
    dummy_df = pd.get_dummies(data=titanic[['sex','embark_town']], drop_first=True)
    titanic = pd.concat([titanic, dummy_df], axis=1)
    titanic=titanic.drop(columns=['Unnamed: 0', 'sex', 'embark_town'])
    imputer=SimpleImputer(strategy='median')
    titanic['age']=imputer.fit_transform(titanic[['age']])
    
    return titanic
    


def prep_telco(telco):
    '''
    This function takes in the telco data acquired by get_telco_data,
    Does encoding, dropes unnecary columns, creates and concats dummies.
    returns cleaned up ready to explore data.
    '''
    
    telco['gender_encoded'] = telco.gender.map({'Female': 1, 'Male': 0})
    telco['partner_encoded'] = telco.partner.map({'Yes': 1, 'No': 0})
    telco['dependents_encoded'] = telco.dependents.map({'Yes': 1, 'No': 0})
    telco['phone_service_encoded'] = telco.phone_service.map({'Yes': 1, 'No': 0})
    telco['paperless_billing_encoded'] = telco.paperless_billing.map({'Yes': 1, 'No': 0})
    telco['churn_encoded'] = telco.churn.map({'Yes': 1, 'No': 0})
    
    dummy_df = pd.get_dummies(telco[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type_id', \
                              'internet_service_type', \
                              'payment_type'
                            ]],
                              drop_first=True)
    telco = pd.concat( [telco, dummy_df], axis=1 )
    telco=telco.drop(columns=['internet_service_type_id', 'contract_type_id.1', 'payment_type_id', 'multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type_id', \
                              'payment_type', \
                                'Unnamed: 0'])
    
    return telco






def my_train_test_split(df, target):
    '''takes a dataframe and target. splits the dataframe into train and split with the test size .2.
    And then takes train data splits it into train and validate. validate size.25
    returns 3 datasets train, validate and test'''
    
    train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[target])
    train, validate = train_test_split(train, test_size=.25, random_state=123, stratify=train[target])
    
    return train, validate, test