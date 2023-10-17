import pandas as pd

class DataHandler:
    def __init__(self):
        pass

    def clean_data(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        if dataframe.empty:
            print("Error: The data is empty. Please load the property data first.")
            return pd.DataFrame()

        # Removing rows with missing values
        cleaned_data = dataframe.dropna()

        # Removing rows with negative values in 'price' and 'land_size' columns
        #cleaned_data = cleaned_data[cleaned_data['price'] >= 0]
        #cleaned_data = cleaned_data[cleaned_data['land_size'] >= 0]

        print("Data cleaned successfully.")
        return cleaned_data


    def efficient_storage(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        if dataframe.empty:
            print("Error: The data is empty. Please load the property data first.")
            return pd.DataFrame()

        # Convert data to efficient types for storage
        for col in dataframe.select_dtypes(include=['float']):
            dataframe[col] = pd.to_numeric(dataframe[col], downcast='float')

        for col in dataframe.select_dtypes(include=['int']):
            dataframe[col] = pd.to_numeric(dataframe[col], downcast='integer')

        print("Data stored efficiently.")
        return dataframe
