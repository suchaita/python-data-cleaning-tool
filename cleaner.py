# Module (reusable component)

import pandas as pd
# self = current object, df = data frame, column_name = name of the column to be cleaned, output_path = path where the cleaned data will be saved, path = path to the CSV file to be loaded.
class DataCleaner:

    def __init__(self, path): # Initialize the DataCleaner with the path to the CSV file
        self.path = path 
        self.df = None # Initialize the DataFrame to None

    def load_data(self): 
        self.df = pd.read_csv(self.path) # Load the CSV file into a DataFrame

    def remove_duplicates(self): 
        self.df = self.df.drop_duplicates() # Remove duplicate rows from the DataFrame. drop_duplicates()- is a method belonging to a specific  Pandas DataFrame object (or Series object),  that removes duplicate rows from a DataFrame. It returns a new DataFrame with duplicate rows removed. By default, it considers all columns to identify duplicates, but you can specify specific columns to check for duplicates using the subset parameter. The function also has an inplace parameter that allows you to modify the original DataFrame directly without creating a new one. If inplace=True, the original DataFrame will be modified and the function will return None. If inplace=False (default), a new DataFrame with duplicates removed will be returned, and the original DataFrame will remain unchanged.

    def clean_column(self, column_name):
        if column_name not in self.df.columns:
            print(f"Column '{column_name}' not found.")
            return
        
        self.df[column_name] = (
            self.df[column_name]
            .fillna("Unknown", inplace=False)   # Fill any missing values in the specified column with an empty string
        )

    def save_data(self, output_path):
        self.df.to_csv(output_path, index=False) # Save the cleaned DataFrame to a new CSV file at the specified output path, without including the index in the output file.
