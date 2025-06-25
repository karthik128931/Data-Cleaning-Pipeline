from src.data_cleaning_pipeline import automated_data_cleaning_pipeline

# Ask the user for the dataset name
dataset_name = input("Enter the dataset name (e.g., raw_data.csv): ")

# Construct the file path
filepath = f"data/{dataset_name}"

# Run the data cleaning pipeline
cleaned_data = automated_data_cleaning_pipeline(filepath)

# Save the cleaned data to a CSV file
cleaned_data.to_csv(f"data/cleaned_{dataset_name}", index=False)
