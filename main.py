"""Entry point for the sample CSV cleaning workflow."""

from pathlib import Path

from cleaner import DataCleaner


PROJECT_DIR = Path(__file__).resolve().parent


def main():
    input_path = PROJECT_DIR / "data" / "sample_data.csv"
    output_path = PROJECT_DIR / "data" / "cleaned_output.csv"

    cleaner = DataCleaner(input_path)
    cleaner.load_data()

    print("Original data:")
    print(cleaner.df.head())

    removed_rows = cleaner.remove_duplicates()
    cleaner.clean_column("name")
    cleaner.clean_column("Cabin")

    cleaner.save_data(output_path)

    print(f"\nDuplicate rows removed: {removed_rows}")
    print(f"Cleaned data saved to: {output_path}")
    print("\nCleaned data preview:")
    print(cleaner.df.head())


if __name__ == "__main__":
    main()
