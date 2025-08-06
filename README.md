# DATA-PIPELINE-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MAYANK SHARMA

*INTERN ID*: CT04DZ2045

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## DECSRIPTION OF THE TASK: The task involves designing and implementing a robust ETL (Extract, Transform, Load) pipeline using Python, specifically leveraging the capabilities of Pandas and Scikit-learn. The goal is to automate the data preprocessing and transformation workflow for a dataset, ensuring that it is clean, consistent, and ready for downstream tasks such as analysis or machine learning. For demonstration purposes, the Titanic dataset—a well-known dataset available through the Seaborn library—is used as the input source.

Objective:
The primary objective is to create a modular and reusable Python script that performs the following:

Extracts raw data from a built-in source.

Transforms the data by handling missing values, encoding categorical variables, and scaling numerical features.

Loads the processed data into a structured format (CSV) for future use.

This pipeline is designed to be adaptable to other datasets with similar characteristics and can be extended to include additional preprocessing steps if needed.

Dataset Overview:
The Titanic dataset contains information about passengers aboard the RMS Titanic, including features such as age, sex, fare, class, number of siblings/spouses aboard, and survival status. It includes both numerical and categorical data, as well as missing values, making it an ideal candidate for demonstrating preprocessing techniques.

Tools and Libraries:
Pandas: Used for data manipulation and I/O operations.

Seaborn: Provides access to the Titanic dataset.

Scikit-learn: Powers the transformation pipeline, including imputation, scaling, encoding, and pipeline orchestration.

Joblib: Used to serialize and save the preprocessing pipeline for reuse.

ETL Pipeline Breakdown:
1. Extract Phase The extraction step loads the Titanic dataset using seaborn.load_dataset('titanic'). This eliminates the need for external files and ensures consistent data access. The dataset is loaded into a Pandas DataFrame for easy manipulation.

2. Transform Phase This phase is the core of the pipeline. It involves several preprocessing steps:

Column Filtering: Columns with excessive missing values (deck, embark_town) or redundant information (alive, class, who) are dropped.

Feature Identification: Columns are categorized into numerical and categorical features based on their data types.

Imputation: Missing values in numerical columns are filled with the mean, while categorical columns are filled with the most frequent value.

Scaling: Numerical features are standardized using StandardScaler to ensure uniformity.

Encoding: Categorical features are transformed using OneHotEncoder, converting them into binary vectors suitable for machine learning models.

Pipeline Construction: These steps are encapsulated in Scikit-learn’s Pipeline and ColumnTransformer objects, enabling clean and modular transformations.

Serialization: The fitted preprocessing pipeline is saved using joblib.dump() for future reuse, ensuring consistency across different runs.

3. Load Phase The transformed data, now in NumPy array format, is converted back into a Pandas DataFrame and saved as a CSV file (titanic_processed.csv). This step ensures that the processed data is accessible for further analysis or modeling.

Deliverables:
A Python script (DataPipelineDevelopment.py) containing the complete ETL pipeline.

A CSV file (titanic_processed.csv) with the transformed data.

A serialized preprocessing pipeline (titanic_preprocessor.pkl) for reuse.

# OUTPUT:

<img width="2880" height="1200" alt="Image" src="https://github.com/user-attachments/assets/213af830-7726-4b18-8b35-71e463db24b1" />
