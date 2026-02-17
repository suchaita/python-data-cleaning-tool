# 🧹 Python Data Cleaning Tool

A modular data cleaning tool built using Python and Pandas.  
This project demonstrates clean architecture, reusable components, and structured execution using the `__main__` entry-point pattern.

---

## 📌 Project Overview

This tool loads a CSV dataset, performs basic cleaning operations, and saves the cleaned output to a new file.

The project is structured with:
- A reusable logic module (`cleaner.py`)
- An execution entry-point (`main.py`)
- A separate `data/` directory for input and output files

This design follows real-world Python project structure and separation of concerns.

---

## 🗂 Project Structure

python-data-cleaning-tool/
    main.py # Entry-point script
    cleaner.py # Reusable data cleaning module
    data/
        sample_data.csv # Input dataset
        cleaned_output.csv # Generated cleaned output


---

## ⚙️ Features

- Load CSV files using Pandas
- Remove duplicate rows
- Clean specific columns
  - Handle missing values (`NaN`)
  - Replace missing values with `"Unknown"`
- Save cleaned data to a new CSV file
- Clear separation between logic and execution

---

## 🧠 Technical Design

### `cleaner.py`
Contains the `DataCleaner` class responsible for:
- Loading data
- Removing duplicates
- Cleaning selected columns
- Saving output

This file acts as a reusable module.

---

### `main.py`
Acts as the entry-point script.

---

## 📊 Output

The script will:

- Print the first 5 rows of the original dataset  
- Perform cleaning operations  
- Save cleaned data to: data/cleaned_output.csv

---
## 🎯 Purpose

This project was built to demonstrate:

- Object-Oriented Programming (OOP)
- Modular Python design
- Clean execution control using `__name__`
- Practical Pandas usage
- Debugging and structured development

---

## 📌 Future Improvements

- Add logging instead of print statements
- Add CLI argument support for file paths
- Add automated column detection
- Add data validation checks
- Add unit tests

---

## 🎯 Purpose

This project was built to demonstrate:

- Object-Oriented Programming (OOP)
- Modular Python design
- Clean execution control using `__name__`
- Practical Pandas usage
- Debugging and structured development

---

## 📌 Future Improvements

- Add logging instead of print statements
- Add CLI argument support for file paths
- Add automated column detection
- Add data validation checks
- Add unit tests

---

## 👩‍🎓 Author
**Suchaita Halder**  
Student | Machine Learning Learner
Developed as part of internship preparation to demonstrate structured Python development and data handling skills.