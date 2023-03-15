# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The loan approval process is a critical component of many businesses, but traditional methods can be slow, error-prone, and inefficient. One solution to these problems is to automate the loan approval process using machine learning. By analyzing large amounts of data, machine learning algorithms can identify patterns and relationships that can be used to make more accurate and efficient loan decisions. However, developing and implementing a machine learning-based loan approval system is a complex process that requires careful attention to data integration, model development, and testing.


## Hypothesis
To generate a hypothesis for research related to loan approval, it is important to identify all potential factors that could impact the outcome. The following hypotheses are proposed:

Income: Applicants with a higher combined income may have a greater chance of being approved for a loan.
Education: Applicants with a higher level of education, such as a graduate degree, may be more likely to be approved for a loan.
Loan amount: Applicants requesting a smaller loan amount may have a higher probability of being approved.
Loan term: Loans with shorter terms may be more likely to be approved.
Credit history: Applicants who have a history of repaying their debts on time may be more likely to be approved for a loan.


## EDA 
Since we are working on loan applications, it is better to be on safer side and reject deserving applications than approving risky ones. I used the same philosophy for imputing values.
Attribute Missing Values Treatment 
Gender 13 Random as Male/Female
Married 3 Random as Yes/No 
Self_Employed 32 Random as Yes/No 
Dependents 15 Maximum from dataset. More dependent for stress test.
LoanAmount 22 Minimum from dataset. Approve for lowest loan amount.
Loan_Amount_Term 14 Minimum from dataset. Shortest tenure loan means low risk.
Credit_History 50 Hard-code to 0. Assume no credit history.

## Process
Step 1 Data Exploration
I analysed at the dataframe to check how many features have missing values.
I also looked at basic statistics for the numeric variables.
I looked at the applicant income and found the data is skewed with outliers.
I also looked at the co-applicant income and found many records with zero income (mostly for unmarried applicants and married but non-working spouses).
I looked at the applicant income by education and identified that Graduate applicants make higher income
I applied pivot tables to look at mean income by property area and education. It seems the educated candidates have almost twice income irrespective of area.
I applied pivot tables to look at mean income by employment type and education. Irrespective of educational qualification, self-employed applicants had more income

Step 2 Data Cleaning
I applied the log scaling on the applicant income and see the skewness is slightly addressed.

Step 3 Building a Predictive Model
Logistic Regression showed an Accuracy of 73.11%
Later, paramater grid search was used to improve the results
The Best parameters: {'classifier__max_depth': None, 'classifier__max_features': 'auto', 'classifier__min_samples_leaf': 1, 'classifier__min_samples_split': 2, 'classifier__n_estimators': 50}

Step 4 Using Pipeline
Pipeline was created to take one row of the dataset and predict the probability of being granted a loan.

Step 5 Deploying ML
Machine learning model was deployed using Flask

## Results/Demo
The pipeline was tested using Python code followed by API calls using Postman

## Challanges 
Since I am using EC2 free tiers, the instance kept shutting off (maybe ephemeral)
This resulted in longer time to keep creating and configuration of instances

## Future Goals
Fine tune the flask for error handling