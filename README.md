# Classification Project

*Welcome to my very first project with Machine Learning*
***

## Project Objectives

- Document code, process (data acquistion, preparation, exploratory data analysis and statistical testing, modeling, and model evaluation), findings, and key takeaways in a Jupyter Notebook report.


- Create modules (acquire.py, prepare.py) that make my process repeateable.


- Construct a model to predict customer churn using classification techniques.


- Deliver a 5 minute presentation consisting of a high-level notebook walkthrough using my Jupyter Notebook from above; my presentation should be appropriate for my target audience.


- Answer panel questions about my code, process, findings and key takeaways, and model.
***


## Business Goals

- Find drivers for customer churn at Telco. Why are customers churning?


- Construct a ML classification model that accurately predicts customer churn.


- Document your process well enough to be presented or read like a report.
***

## Audience

- My target audience for your notebook walkthrough is the Codeup Data Science team.
***

## Deliverables

I expect to deliver the following:

- a Jupyter Notebook Report showing process and analysis with the goal of finding drivers for customer churn. This notebook should be commented and documented well enough to be read like a report or walked through as a presentation.


- a README.md file containing the project description with goals, initial hypotheses, a data dictionary, project planning, instructions or an explanation of how someone else can recreate my project and findings (What would someone need to be able to recreate my project on their own?), answers to my hypotheses, key findings, recommendations, and takeaways from my project.
    

- a CSV file with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn). These predictions will be from my best performing model ran on X_test.


- individual modules, .py files, that hold my functions to acquire and prepare my data.


- a notebook walkthrough presentation with a high-level overview of my project (5 minutes max). I will be prepared to answer follow-up questions about my code, process, tests, model, and findings.
***

## Project Planning
**Plan->** Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver

- Create Readme.md that describes the project and goals.


- Create an acquire.py and prepare.py file to acquire the telco data set, prepare and select my features and split it into  train validate and test dataframes.  


- Create and update a data dictionary for those reading the project


- Document my project in a way that passes the wife test (can my wife who isnt into data science understand what is happening)


- Clearly state my starting hypotheses (and add the testing of these to my task list).


## Data Acquisition

Plan -> **Acquire** -> Prepare -> Explore -> Model & Evaluate -> Deliver

Make an acquire.py module that:

Stores functions that are needed to acquire data from the customers table from the telco_churn database on the Codeup data science database server; make sure my module contains the necessary imports to run my code. 

My final function will return a pandas DataFrame.



## Data dictionary
| Feature                  | Datatype               | Definition   |
|:-------------------------|:-----------------------|:-------------|
| payment_type_id          | 7043 non-null: int64   | Indication of how customer paid their bill: 1 = Electronic check, 2 = Mailed check, 3 = Bank transfer (automatic), 4 =Credit card (automatic)         |
| contract_type_id         | 7043 non-null: int64   |Contract the customer holds 1 = Month to month , 2 = One year contract , 3 =Two year contract     |
| internet_service_type_id | 7043 non-null: int64   |Intenet type the customer has: 1 = DSL , 2 = Fiber Optic , 3 = No Internet               |
| customer_id              | 7043 non-null: object  |Unique value for each customer used for identification |
| gender                   | 7043 non-null: object  |Customer Gender: male or female|
| senior_citizen           | 7043 non-null: int64   |Is the customer a senior citizen: 0= no 1=yes |
| partner                  | 7043 non-null: object  |Does the customer have a partner: yes or no   |
| dependents               | 7043 non-null: object  |Does the customer have dependents: yes or no  |
| tenure                   | 7043 non-null: int64   |How long the customer has been with the company in months              |
| phone_service            | 7043 non-null: object  |Does the customer have phone service:  yes or no|
| multiple_lines           | 7043 non-null: object  |Does the customer have multiple lines:  yes or no|
| online_security          | 7043 non-null: object  |Does the customer have online security: Yes, no, or no internet service |
| online_backup            | 7043 non-null: object  |Does the customer have online backup: Yes, no, or no internet service|
| device_protection        | 7043 non-null: object  |Does the customer have device protection: Yes, no, or no internet service|
| tech_support             | 7043 non-null: object  |Does the customer have tech support: Yes, no, or no internet service|
| streaming_tv             | 7043 non-null: object  |Does the customer have streaming tv: Yes, no, or no internet service|
| streaming_movies         | 7043 non-null: object  |Does the customer have streaming movies: Yes, no, or no internet service|
| paperless_billing        | 7043 non-null: object  |Does the customer have paperless billing: Yes, no, or no internet service|
| monthly_charges          | 7043 non-null: float64 |The amount the customer is charged monthly     |
| total_charges            | 7043 non-null: object  |The total amount the customer has been billed |
| churn                    | 7043 non-null: object  |Has the customer left: yes or no|
| internet_service_type    | 7043 non-null: object  |The type of internet service the customer has|
| contract_type            | 7043 non-null: object  |The type of contract the customer has|
| payment_type             | 7043 non-null: object  |The type of payment the customer uses              |
