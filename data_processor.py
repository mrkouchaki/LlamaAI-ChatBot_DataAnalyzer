# data_processor.py

import pandas as pd

# Function to load CSV data
def load_csv(file_path):
    """
    Loads a CSV file into a pandas DataFrame.
    
    :param file_path: Path to the CSV file.
    :return: A pandas DataFrame containing the CSV data, or an error message.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        return f"Error loading CSV file: {e}"

# Function to process CSV data and provide summary statistics
def summarize_data(data):
    """
    Provides summary statistics for the given DataFrame.
    
    :param data: A pandas DataFrame.
    :return: A string containing the summary statistics.
    """
    if isinstance(data, pd.DataFrame):
        summary = data.describe()  # Get summary statistics
        return summary.to_string()
    else:
        return "Invalid data provided."

# Function to display a specific column from the dataset
def display_column(data, column_name):
    """
    Displays a specific column from the DataFrame.
    
    :param data: A pandas DataFrame.
    :param column_name: The name of the column to display.
    :return: A string with the column data or an error message if column is not found.
    """
    if isinstance(data, pd.DataFrame):
        if column_name in data.columns:
            return data[column_name].to_string(index=False)
        else:
            return f"Column '{column_name}' not found in the dataset."
    else:
        return "Invalid data provided."
