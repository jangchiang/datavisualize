from SimpleDataAnalyser import SimpleDataAnalyser
from DataVisualiser import DataVisualiser
from PropertyFinder import PropertyFinder
from DataHandler import DataHandler

class InvestorApplication:
    def __init__(self):
        self.analyser = SimpleDataAnalyser()
        self.visualiser = DataVisualiser()
        self.finder = PropertyFinder()
        self.handler = DataHandler()
        self.data = None

    def display_menu(self):
        print("\nInvestor Application Menu:")
        print("1. Load Property Data")
        print("2. Currency Exchange")
        print("3. Suburb Property Summary")
        print("4. Average Land Size")
        print("5. Property Value Distribution")
        print("6. Sales Trend")
        print("7. Locate Specific Property Price")
        print("8. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ").strip()

            if choice == '1':
                file_path = input("Enter the file path to the property data CSV: ").strip()
                self.data = self.analyser.extract_property_info(file_path)
                self.data = self.handler.clean_data(self.data)
                self.data = self.handler.efficient_storage(self.data)

            elif choice == '2':
                exchange_rate = float(input("Enter the exchange rate to convert property prices: ").strip())
                self.data = self.analyser.currency_exchange(self.data, exchange_rate)

            elif choice == '3':
                suburb = input("Enter the suburb (or 'all' for all suburbs): ").strip()
                self.analyser.suburb_property_summary(self.data, suburb)

            elif choice == '4':
                suburb = input("Enter the suburb (or 'all' for all suburbs): ").strip()
                print("Average land size:", self.analyser.avg_land_size(self.data, suburb))

            elif choice == '5':
                suburb = input("Enter the suburb (or 'all' for all suburbs): ").strip()
                target_currency = input("Enter the target currency (default is AUD): ").strip() or "AUD"
                self.visualiser.prop_val_distribution(self.data, suburb, target_currency)

            elif choice == '6':
                self.visualiser.sales_trend(self.data)

            elif choice == '7':
                suburb = input("Enter the suburb: ").strip()
                target_price = float(input("Enter the target property price: ").strip())
                if self.finder.locate_price(target_price, self.data, suburb):
                    print(f"A property with price {target_price} found in {suburb}.")
                else:
                    print(f"No property with price {target_price} found in {suburb}.")

            elif choice == '8':
                print("Thank you for using the Investor Application. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    app = InvestorApplication()
    app.run()
