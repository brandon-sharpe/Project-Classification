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

Make anacquire.py module that:

Store functions that are needed to acquire data from the customers table from the telco_churn database on the Codeup data science database server; make sure my module contains the necessary imports to run my code. 

My final function will return a pandas DataFrame.



## Data dictionary
Target  | Description   | Data Type
--|--|--
churn   | indicates whether or not a customer churned | int64



Categorical Features   | Description |	Data Type
--|--|--
senior_citizen|	indicates if the customer is a senior citizen	|int64
dependents|	    indicates if the customer has dependents	|int64
phone_service|	indicates if the customer has phone service with Telco	| int64
multiple_lines |	indicates if the customer with phone service has multiple lines	| int64
online_security|	indicates if the customer has online security services |	int 64
online_backup|	indicates if the customer has online backup services |	int64
device_protection	| indicates if the customer has device protection services |	int64
tech_support |  indicates if the customer has tech support services |	int64
streaming_tv |	indicates if the customer has tv streaming services |	int64
streaming_movies |	indicates if the customer has movie streaming services |	int64
payment_type    | indicates the type of payment method a customer is using | int64
internet_service_type |	indicates which internet service (if any) the customer has |	int64
gender	|   indicates the the customers' gender identity |	uint8
contract_type | 	indicates the type of contract the customer has with Telco |	int64
auto_bill_pay |	indicates if the customer is enrolled in auto bill pay or not |	int64

Continuous Features | Description | Data Type
--|--|--
monthly_charges | how much a customer pays per month in dollars| float64
total_charges   | how much a customer has paid over the course of their tenure | float64
tenure          | how many months the customer has been with the company| int64

Other   | Description   | Data Type
--|--|--
customer_id | customer id number                       | object

