import pandas as pd

class PropertyFinder:
    def __init__(self):
        pass

    def reverse_insertion_sort(self, prices: list) -> list:
        for i in range(1, len(prices)):
            key = prices[i]
            j = i - 1
            while j >=0 and key > prices[j]:
                prices[j + 1] = prices[j]
                j -= 1
            prices[j + 1] = key
        return prices

    def recursive_binary_search(self, prices: list, low: int, high: int, target_price: float) -> bool:
        if high >= low:
            mid = low + (high - low) // 2

            if prices[mid] == target_price:
                return True

            elif prices[mid] > target_price:
                return self.recursive_binary_search(prices, mid + 1, high, target_price)

            else:
                return self.recursive_binary_search(prices, low, mid - 1, target_price)

        else:
            return False

    def locate_price(self, target_price: float, data: pd.DataFrame, target_suburb: str) -> bool:
        try:
            filtered_data = data[data['suburb'].str.lower() == target_suburb.lower()]['price'].dropna().tolist()

            if not filtered_data:
                print(f"No property data available for the suburb '{target_suburb}'.")
                return False

            sorted_prices = self.reverse_insertion_sort(filtered_data)
            return self.recursive_binary_search(sorted_prices, 0, len(sorted_prices) - 1, target_price)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
