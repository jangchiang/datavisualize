import unittest
import pandas as pd
from SimpleDataAnalyser import SimpleDataAnalyser  # Adjust the import based on your project structure

class TestSimpleDataAnalyser(unittest.TestCase):
    def setUp(self):
        self.analyser = SimpleDataAnalyser()
        self.data = pd.DataFrame({
            'suburb': ['Suburb1', 'Suburb2', 'Suburb3'],
            'price': [500000, 600000, None],
            'land_size': [150, None, 200]
        })

    def test_extract_property_info(self):
        # Test file not found error
        with self.assertRaises(FileNotFoundError):
            self.analyser.extract_property_info("non_existent_file.csv")

        # Add more tests for different scenarios and edge cases

    def test_avg_land_size(self):
        avg_land_size = self.analyser.avg_land_size(self.data, 'Suburb1')
        self.assertEqual(avg_land_size, 150)

        # Test with a non-existent suburb
        avg_land_size = self.analyser.avg_land_size(self.data, 'NonExistent')
        self.assertIsNone(avg_land_size)

        # Add more tests for different scenarios and edge cases

if __name__ == "__main__":
    unittest.main()
