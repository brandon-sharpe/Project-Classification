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
***

## Data Acquisition

Plan -> **Acquire** -> Prepare -> Explore -> Model & Evaluate -> Deliver

Make an acquire.py module that:

Stores functions that are needed to acquire data from the customers table from the telco_churn database on the Codeup data science database server; make sure my module contains the necessary imports to run my code. 

My final function will return a pandas DataFrame.
***

## Data Preparation

Plan -> Acquire -> **Prepare** -> Explore -> Model & Evaluate -> Deliver



Store functions that are needed to prepare my data
My final function should do the following:

- Split my data into train/validate/test.

- Handle Missing Values.

- Handle erroneous data and/or outliers I wish to address.

- Encode variables as needed.

Store it to a well documented prepare.py 
***

## Data Exploration & Analysis

Plan -> Acquire -> Prepare -> **Explore** -> Model & Evaluate -> Deliver

###### Hypothesis 1
${H}_{0}$ Month to month customers and churn are independent

${H}_{a}$ Month to month customers and churn are not independent of each other 

###### Hypothesis 2
${H}_{0}$ Customers with 2 year contracts and churn are independent

${H}_{a}$ Customers with 2 year contracts customers and churn are not independent of each other 

###### Hypothesis 3
${H}_{0}$ Customers with fiber oprtic internet and churn are independent

${H}_{a}$ Customers with fiber optic internet  and churn are not independent of each other 

###### Hypothesis 4
${H}_{0}$ Customers with online security and churn are independent

${H}_{a}$ Customers with online security and churn are not independent of each other 

###### Hypothesis 5
${H}_{0}$ Customers who pay with electronic check and churn are independent

${H}_{a}$ Customers who pay with electronic check are not independent of each other 

###### Hypothesis 6
${H}_{0}$ Tenure and churn are independent

${H}_{a}$ Tenure and churn are not independent

#### After running statistical test I feel confident these are drivers these will be my features.
***

## Modeling and Evaluation

Plan -> Acquire -> Prepare -> Explore -> **Model & Evaluate**-> Deliver

Ran 20 decision trees, 20 randon forest and 20 knn models and took the best perfoming model 
***

## Delivering

Plan -> Acquire -> Prepare -> Explore -> Model & Evaluate -> **Deliver

Introduce myself and my project goals at the very beginning of my notebook walkthrough.

Summarize my findings at the beginning.

Walk through my analysis.



Finish with key takeaways, recommendations, and next steps and be prepared to answer questions from the data science team about your project.
***




## Data dictionary(Pre-cleaning)
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
***

## Data dictionary(Post-Cleaning)
| Feature                    | Datatype               | Definition   |
|:---------------------------|:-----------------------|:-------------|
| customer_id                | 3943 non-null: object  |Unique value for each customer used for identification|
| senior_citizen             | 3943 non-null: int64   |Is the customer a senior citizen: 0= no 1=yes|
| tenure                     | 3943 non-null: int64   |How long the customer has been with the company in months |
| monthly_charges            | 3943 non-null: float64 |The amount the customer is charged monthly |
| total_charges              | 3943 non-null: float64 |The total amount the customer has been billed|
| is_male                    | 3943 non-null: uint8   |Is the customer male: 0= no 1=yes |
| has_partner                | 3943 non-null: uint8   |Does the customer have a partner: 0= no 1=yes|
| has_dependents             | 3943 non-null: uint8   |Does the customer have dependents: 0= no 1=yes|
| has_phone_service          | 3943 non-null: uint8   |Does the customer phone service: 0= no 1=yes|
| has_multiple_lines         | 3943 non-null: uint8   |Does the customer have multiple lines: 0= no 1=yes|
| has_online_security        | 3943 non-null: uint8   |Does the customer have online security: 0= no 1=yes|
| has_online_backup          | 3943 non-null: uint8   |Does the customer have online backup: 0= no 1=yes|
| has_device_protection      | 3943 non-null: uint8   |Does the customer have device protection: 0= no 1=yes|
| has_tech_support           | 3943 non-null: uint8   |Does the customer have tech support: 0= no 1=yes|
| has_streaming_tv           | 3943 non-null: uint8   |Does the customer have tv streaming: 0= no 1=yes|
| has_streaming_movies       | 3943 non-null: uint8   |Does the customer have movie streaming: 0= no 1=yes|
| has_paperless_billing      | 3943 non-null: uint8   |Does the customer have paperless billing: 0= no 1=yes|
| has_churned                | 3943 non-null: uint8   |Has the customer left the company: 0= no 1=yes|
| automatic_payment          | 3943 non-null: int64   |Does the customer have automatic payments: 0= no 1=yes|
| has_dsl                    | 3943 non-null: uint8   |Does the customer have DSL: 0= no 1=yes|
| has_fiber                  | 3943 non-null: uint8   |Does the customer have Fiber Optic: 0= no 1=yes|
| has_no_internet            | 3943 non-null: uint8   |Does the customer not have internet : 0= no 1=yes|
| month_to_month_customer    | 3943 non-null: uint8   |Does the customer have a month to month contract: 0= no 1=yes |
| contract_customer_one_year | 3943 non-null: uint8   |Does the customer have a One year contract: 0= no 1=yes   |
| contract_customer_two_year | 3943 non-null: uint8   |Does the customer have a Two year contract: 0= no 1=yes              |
| pays_by_bank_transfer      | 3943 non-null: uint8   |Does the customer pay by bank transfer: 0= no 1=yes|
| pays_by_credit_card        | 3943 non-null: uint8   |Does the customer pay by credit card: 0= no 1=yes|
| pays_by_electronic_check   | 3943 non-null: uint8   |Does the customer pay by electronic check: 0= no 1=yes|
| pays_by_mailed_check       | 3943 non-null: uint8   |Does the customer pay by mailed check: 0= no 1=yes|


*** 

## Conclusion
- I found some the key factors that drive churn
    - Month to Month customers are more likely to churn
    - Customers with fiber internet are more likely to churn
    - Customers who pay by electronic check are more likley to churn
    - Customers who have two year contracts are less likely to churn
    - Customers who recieve more from the company (ex. online security, tech support) are less likely to churn
- My Random forest 1 provides 79% accuracy and a 95% recall.
- Baseline was 73%
*** 

## Recommendation
- Model will allow us to succesfully focus on the customers who are still with us, so we can focus on building their loyalty
- I recommend revisiting our fiber optic plan. As this plan brings in our highest paying customers we should include everything we can to please this customer. I would also reccomend cutting the cost of month to month plans by offering an inncentive to stay longer, stay 11 months and the 12 month is free to try and curb the monthly visitors leaving

*** 

## Reproduction
Dowload the README.MD file along with the acquire.py, prepare.py, telco_churn.csv and the Final.ipynb. Run the Final.ipynb in the same folder as your env.py, acquire.py, telco_churn.csv and prepare.py

