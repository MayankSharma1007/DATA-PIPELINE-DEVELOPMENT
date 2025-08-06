import pandas as pd
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import joblib

# Step 1: Extract
def extract_data():
    """Load Titanic dataset from Seaborn."""
    return sns.load_dataset('titanic')

# Step 2: Transform
def transform_data(df):
    """Preprocess and transform the Titanic dataset."""

    # Drop columns with too many missing values or irrelevant info
    df = df.drop(columns=['deck', 'embark_town', 'alive', 'class', 'who'])

    # Identify column types
    numeric_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()

    # Numeric pipeline
    numeric_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    # Categorical pipeline
    categorical_pipeline = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    # Combine pipelines
    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_pipeline, numeric_features),
        ('cat', categorical_pipeline, categorical_features)
    ])

    # Fit and transform
    transformed_data = preprocessor.fit_transform(df)

    # Save the preprocessor for future use
    joblib.dump(preprocessor, 'titanic_preprocessor.pkl')

    return transformed_data

# Step 3: Load
def load_data(transformed_data, output_path):
    """Save the transformed Titanic data to a CSV file."""
    pd.DataFrame(transformed_data).to_csv(output_path, index=False)

# Main ETL function
def run_etl(output_path):
    df = extract_data()
    transformed_data = transform_data(df)
    load_data(transformed_data, output_path)
    print("ETL process completed successfully.")

# Example usage
if __name__ == "__main__":
    output_csv = 'titanic_processed.csv'
    run_etl(output_csv)
