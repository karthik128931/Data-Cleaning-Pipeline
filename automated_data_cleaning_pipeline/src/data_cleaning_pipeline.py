import pandas as pd
def load_data(filepath):
    """
    Load the data from a csv file.
    """
    return pd.read_csv(filepath)
from sklearn.impute import SimpleImputer

def handle_missing_values(df):
    """
    Handle missing values in the DataFrame.
    """
    # Impute missing values for numerical columns
    numerical_imputer = SimpleImputer(strategy="mean")
    for column in df.select_dtypes(include=["float64", "int64"]).columns:
        df[column] = numerical_imputer.fit_transform(df[[column]])

    # Impute missing values for categorical columns
    categorical_imputer = SimpleImputer(strategy="most_frequent")
    for column in df.select_dtypes(include=["object"]).columns:
        df[column] = categorical_imputer.fit_transform(df[[column]]).ravel()  # Flatten to 1D

    print("Missing values handled")
    return df

def remove_duplicates(df):
    """
    Remove duplicate rows from the DataFrame.
    """
    df = df.drop_duplicates()
    print("Duplicates removed")
    return df
from scipy import stats

def remove_outliers(df, numeric_columns, z_thresh=3):
    """
    Remove outliers from numerical columns in the DataFrame based on Z-score.
    
    Parameters:
    - df: The DataFrame.
    - numeric_columns: List of column names in which to check for outliers.
    - z_thresh: Z-score threshold to identify outliers. Default is 3.
    
    Returns:
    - The DataFrame with outliers removed.
    """
    for column in numeric_columns:
        # Calculate Z-scores for each value in the column
        z_scores = stats.zscore(df[column])
        
        # Only keep rows where Z-score is within the threshold
        df = df[(z_scores < z_thresh) & (z_scores > -z_thresh)]
    
    print("Outliers removed")
    return df

from sklearn.preprocessing import LabelEncoder
def encode_categorical(df):
    """
    Encode categorical variables using Label Encoding.
    """
    for column in df.select_dtypes(include=["object"]).columns:
        le=LabelEncoder()
        df[column]=le.fit_transform(df[column])
    return df
from sklearn.preprocessing import StandardScaler
def scale_data(df,columns):
    """
    Scale numeric columns using StandardScaler.
    """
    scaler=StandardScaler()
    df[columns]=scaler.fit_transform(df[columns])
    return df
def automated_data_cleaning_pipeline(filepath):
    """
    Execute the full data claening pipeline.
    """
    df=load_data(filepath)
    df=remove_duplicates(df)
    df=handle_missing_values(df)
    numeric_columns=df.select_dtypes(include=["float64","int64"]).columns
    df=remove_outliers(df,numeric_columns)
    df=encode_categorical(df)
    df=scale_data(df,numeric_columns)
    return df



