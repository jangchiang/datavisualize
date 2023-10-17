import matplotlib.pyplot as plt
import pandas as pd

class DataVisualiser:
    def __init__(self):
        self.currency_dict = {
            "AUD": 1, "USD": 0.66, "INR": 54.25, "CNY": 4.72, 
            "JPY": 93.87, "HKD": 5.12, "KRW": 860.92, "GBP": 0.51, 
            "EUR": 0.60, "SGD": 0.88
        }

    def prop_val_distribution(self, dataframe: pd.DataFrame, suburb: str, target_currency="AUD"):
        if dataframe.empty:
            print("Error: The data is empty. Please load the property data first.")
            return

        if not isinstance(suburb, str) or not suburb:
            print("Error: Invalid suburb name. Please enter a valid suburb name.")
            return

        if target_currency not in self.currency_dict:
            print(f"Error: Currency {target_currency} not supported. Displaying in AUD.")
            target_currency = "AUD"

        exchange_rate = self.currency_dict[target_currency]
        dataframe['price'] = dataframe['price'] * exchange_rate

        if suburb.lower() == 'all':
            plt.hist(dataframe['price'].dropna(), bins=30, edgecolor='k')
        else:
            plt.hist(dataframe[dataframe['suburb'].str.lower() == suburb.lower()]['price'].dropna(), 
                     bins=30, edgecolor='k')

        plt.title(f'Property Value Distribution in {suburb} (in {target_currency})')
        plt.xlabel('Property Value')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()

    def sales_trend(self, dataframe: pd.DataFrame):
        if dataframe.empty:
            print("Error: The data is empty. Please load the property data first.")
            return

        dataframe['year'] = pd.DatetimeIndex(dataframe['date']).year
        sales_per_year = dataframe.groupby('year').size()

        plt.plot(sales_per_year.index, sales_per_year.values, marker='o', linestyle='-', color='b')
        plt.title('Sales Trend Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Number of Properties Sold')
        plt.grid(True)
        plt.show()
