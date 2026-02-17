# the entry-point module (when executed)

from cleaner import DataCleaner # Import the DataCleaner class from the cleaner module

def main(): # Define the main function that will execute the data cleaning process
    cleaner = DataCleaner("data/sample_data.csv") # Initialize cleaner with input file
    cleaner.load_data() # Call the load_data method to load the CSV file into a DataFrame. This will read the data from the specified CSV file and store it in the df attribute of the DataCleaner object.
    print("Original Data:")
    print(cleaner.df.head(5))
    cleaner.remove_duplicates() # Call the remove_duplicates method to remove duplicate rows from the DataFrame. 
    cleaner.clean_column("name") # Call the clean_column method to clean the specified column (in this case, "name"). This will fill any missing values in the "name" column with an empty string, convert the values to strings, remove leading and trailing whitespace, and convert the values to lowercase.
    cleaner.clean_column("Cabin")
    cleaner.save_data("data/cleaned_output.csv") # Call the save_data method to save the cleaned DataFrame to a new CSV file at the specified output path ("cleaned_output.csv"). This will write the cleaned data to a new CSV file without including the index in the output file.
    print("Data cleaning completed successfully.")
    print(cleaner.df.head(5)) # Print the first 5 rows of the cleaned DataFrame to verify the results.
    #print(cleaner.df.shape)
if __name__ == "__main__": # Check if the script is being run directly (as the main program) and not imported as a module. If this condition is true, the code inside this block will be executed. if the script is imported as a module, the code inside this block will not be executed. as the cleaner.py file is a logic file and not an execution file, it does not need this block, but main.py is an execution file so it needs this block to ensure that the main function is only executed when the script is run directly. 
    main() 
