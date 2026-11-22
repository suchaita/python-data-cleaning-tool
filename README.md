# Python Data Cleaning Tool

A small, reusable CSV data-cleaning project built with **Python** and **Pandas**. It demonstrates how to separate data-processing logic into a reusable class and keep the execution workflow in a dedicated entry-point script.

## Overview

The application reads a CSV file, removes duplicate rows, fills missing values in selected columns, and saves the cleaned dataset to a new CSV file.

The included sample dataset is a Titanic passenger dataset used for demonstration and practice.

## Features

- Load data from a CSV file with Pandas
- Remove duplicate rows
- Fill missing values in selected columns with a configurable value (defaults to `"Unknown"`)
- Save the cleaned dataset as a new CSV file
- Keep reusable cleaning logic separate from the main execution script
- Resolve input and output paths relative to the project, so the script can be run from another working directory

## Project Structure

```text
python-data-cleaning-tool/
├── cleaner.py              # Reusable DataCleaner class
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── .gitignore
└── data/
    ├── sample_data.csv     # Input sample dataset
    └── cleaned_output.csv  # Generated after running the script
```

## Requirements

- Python 3.9 or newer
- Pandas

## Setup and Run

1. Clone the repository and open its directory:

   ```bash
   git clone https://github.com/suchaita/python-data-cleaning-tool.git
   cd python-data-cleaning-tool
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependency:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application from the project directory:

   ```bash
   python main.py
   ```

The cleaned file is written to `data/cleaned_output.csv`. The script also prints a preview of the original and cleaned data.

## Code Organization

### `cleaner.py`

Defines the `DataCleaner` class, which provides methods to:

- Load a CSV file into a DataFrame
- Remove duplicate rows
- Fill missing values in a specified column
- Save the cleaned DataFrame to a CSV file

The class checks that data has been loaded before cleaning or saving. It raises a clear error if a requested column does not exist.

### `main.py`

Coordinates the workflow: creates a `DataCleaner` instance, loads the sample dataset, applies the selected cleaning operations, and saves the result. The `if __name__ == "__main__"` guard ensures the workflow runs only when the script is executed directly.

## Concepts Demonstrated

- Python modules and imports
- Classes, objects, and instance methods
- Separation of concerns and reusable code
- The `if __name__ == "__main__"` entry-point pattern
- CSV handling and basic data cleaning with Pandas
- File paths and exception handling

## Possible Future Improvements

- Add logging instead of print statements
- Support command-line arguments for input and output paths
- Add configurable cleaning strategies and data validation
- Add automated unit tests

## Author

**Suchaita Halder**

A learning project demonstrating modular Python programming and practical data handling.
