import pandas as pd

class SimpleDataAnalyser:
    def __init__(self):
        self.data = pd.DataFrame()

    def extract_property_info(self, file_path: str) -> pd.DataFrame:
        if not isinstance(file_path, str) or not file_path.endswith('.csv'):
            print("Error: Invalid file path. Please provide a valid CSV file path.")
            return pd.DataFrame()

        try:
            self.data = pd.read_csv(file_path)
            print("Property data loaded successfully!")
            return self.data
        
        except FileNotFoundError:
            print("Error: The file was not found.")
            return pd.DataFrame()
        
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            return pd.DataFrame()
        
        except pd.errors.ParserError:
            print("Error: There is an issue with the file content.")
            return pd.DataFrame()
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return pd.DataFrame()

    def currency_exchange(self, dataframe: pd.DataFrame, exchange_rate: float) -> pd.DataFrame:
        if dataframe.empty:
            print("Error: The data is empty. Please load the property data first.")
            return pd.DataFrame()

        if not isinstance(exchange_rate, (int, float)) or exchange_rate <= 0:
            print("Error: Invalid exchange rate. Please enter a positive number.")
            return pd.DataFrame()

        dataframe['price'] = dataframe['price'] * exchange_rate
        return dataframe

    def suburb_property_summary(self, dataframe: pd.DataFrame, suburb: str):
        if dataframe.empty:
            print("Error: The data is empty. Please load the property data first.")
            return

        if not isinstance(suburb, str) or not suburb:
            print("Error: Invalid suburb name. Please enter a valid suburb name.")
            return

        if suburb.lower() == 'all':
            print(dataframe.describe())
        elif suburb.lower() in dataframe['suburb'].str.lower().values:
            print(dataframe[dataframe['suburb'].str.lower() == suburb.lower()].describe())
        else:
            print(f"Error: Suburb '{suburb}' not found in the data.")

    def avg_land_size(self, dataframe: pd.DataFrame, suburb: str) -> float:
        if dataframe.empty:
            print("Error: The data is empty. Please load the property data first.")
            return None

        if not isinstance(suburb, str) or not suburb:
            print("Error: Invalid suburb name. Please enter a valid suburb name.")
            return None

        filtered_data = dataframe[dataframe['land_size'].notnull()]

        if suburb.lower() == 'all':
            return filtered_data['land_size'].mean()

        filtered_data = filtered_data[filtered_data['suburb'].str.lower() == suburb.lower()]

        if filtered_data.empty:
            print(f"Error: Suburb '{suburb}' not found in the data.")
            return None

        return filtered_data['land_size'].mean()
