import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
from sklearn.model_selection import train_test_split
from scipy import stats
from acquire import get_connection, get_telco_churn_data

def clean_telco_df(df):
    # Make total_charges a float instead of an object. 
    df.total_charges = pd.to_numeric(df.total_charges, errors='coerce').astype('float64')
    # Customers with 0 tenure have null values, made total_charges 0 for those customers because they have not yet paid a bill
    df.total_charges = df.total_charges.fillna(value=0)
    # Customers who do not have internet or phone service are the same as those not recieving the extra service by choice.
    df.replace('No internet service', 'No', inplace=True)
    df.replace('No phone service', 'No', inplace = True)
    # encode all non-numeric data that I can afford to drop the first column for
    dummy_df = pd.get_dummies(df[['gender',
                                  'partner',
                                  'dependents',
                                  'phone_service',
                                  'multiple_lines',
                                  'online_security', 
                                  'online_backup', 
                                  'device_protection', 
                                  'tech_support', 
                                  'streaming_tv',
                                  'streaming_movies',
                                  'paperless_billing',
                                  'churn' ]],
                              drop_first=True)
    # create readable column titles
    dummy_df = dummy_df.rename(columns={'gender_Male': 'is_male',
                                   'partner_Yes': 'has_partner',
                                   'dependents_Yes': 'has_dependents',
                                   'phone_service_Yes': 'has_phone_service',
                                   'multiple_lines_Yes': 'has_multiple_lines',
                                   'online_security_Yes': 'has_online_security',
                                   'online_backup_Yes': 'has_online_backup',
                                   'device_protection_Yes': 'has_device_protection',
                                   'tech_support_Yes': 'has_tech_support',
                                   'streaming_tv_Yes': 'has_streaming_tv',
                                   'streaming_movies_Yes': 'has_streaming_movies',
                                   'paperless_billing_Yes': 'has_paperless_billing',
                                   'churn_Yes': 'has_churned'})
    # Drop all columns that i just made an encoding for, also dropped duplicate columns 
    # payment_type_id, contract_type_id,internet_service_type_id. Dropped customer_id as it holds no value
    df = df.drop(columns =['gender',
                       'partner',
                       'dependents',
                       'phone_service',
                       'multiple_lines',
                       'online_security', 
                       'online_backup', 
                       'device_protection', 
                       'tech_support', 
                       'streaming_tv',
                       'streaming_movies',
                       'paperless_billing',
                       'churn',
                       'customer_id',
                       'payment_type_id',
                       'contract_type_id', 
                       'internet_service_type_id'])
    # merge the dummy_df and df
    df = pd.concat([df, dummy_df], axis =1)
    # Seperated payment type and whether or not a payment was automatic
    df["automatic_payment"] =( df.payment_type == ('Bank transfer (automatic)')) | (df.payment_type == ('Credit card (automatic)'))
    df["automatic_payment"] = (df["automatic_payment"]).astype(int)
    # create another df with contract types, payment types, and internet service
    dummy_df2 = pd.get_dummies(df[['internet_service_type','contract_type','payment_type']], drop_first=False )
    #rename dummy table columns
    #rename columns
    dummy_df2 = dummy_df2.rename(columns={'internet_service_type_DSL': 'has_dsl',
                                   'internet_service_type_Fiber optic': 'has_fiber',
                                   'internet_service_type_None': 'has_no_internet',
                                   'contract_type_Month-to-month': 'month_to_month_customer',
                                   'contract_type_One year': 'contract_customer_one_year',
                                   'contract_type_Two year': 'contract_customer_two_year',
                                   'payment_type_Bank transfer (automatic)': 'pays_by_bank_transfer',
                                   'payment_type_Credit card (automatic)': 'pays_by_credit_card',
                                   'payment_type_Electronic check': 'pays_by_electronic_check',
                                   'payment_type_Mailed check': 'pays_by_mailed_check'
                                   })
    #concat new columns for contract types, payment types, amd internet service
    df = pd.concat([df, dummy_df2], axis =1)
    # drop duplicate info columns
    df = df.drop(columns =['internet_service_type',
                       'contract_type',
                       'payment_type'
                       ])
    return df

def telco_split(df):
    #splitting our data
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.has_churned)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.has_churned)
    return train, validate, test


def prep_telco(df):
    #cleaning and splitting our data
    df = clean_telco_df(df)
    train, validate, test = telco_split(df)
    return train, validate, test