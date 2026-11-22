"""Reusable CSV data-cleaning utilities built with Pandas."""

from pathlib import Path

import pandas as pd


class DataCleaner:
    """Load, clean, and save a CSV dataset."""

    def __init__(self, path):
        self.path = Path(path)
        self.df = None

    def _ensure_data_loaded(self):
        """Raise an error when a cleaning operation runs before loading data."""
        if self.df is None:
            raise RuntimeError("No data loaded. Call load_data() before this operation.")

    def load_data(self):
        """Load the configured CSV file into a Pandas DataFrame."""
        self.df = pd.read_csv(self.path)
        return self.df

    def remove_duplicates(self):
        """Remove fully duplicated rows and return the number of rows removed."""
        self._ensure_data_loaded()
        original_count = len(self.df)
        self.df = self.df.drop_duplicates()
        return original_count - len(self.df)

    def clean_column(self, column_name, fill_value="Unknown"):
        """Fill missing values in a column and return the updated Series."""
        self._ensure_data_loaded()

        if column_name not in self.df.columns:
            raise KeyError(f"Column '{column_name}' not found in the dataset.")

        self.df[column_name] = self.df[column_name].fillna(fill_value)
        return self.df[column_name]

    def save_data(self, output_path):
        """Save the cleaned DataFrame to a CSV file without its index."""
        self._ensure_data_loaded()

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        self.df.to_csv(output_path, index=False)
        return output_path
