from src.data_cleaning_pipeline import automated_data_cleaning_pipeline


if __name__=="__main__":
    filepath="data/raw_data.csv"
    cleaned_data=automated_data_cleaning_pipeline(filepath)
    cleaned_data.to_csv("data/cleaned_data.csv",index=False)
    print("Data cleaning complete and saved to 'data/cleaned_data.csv'")
