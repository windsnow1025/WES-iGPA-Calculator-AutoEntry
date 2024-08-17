import pandas as pd


def read_excel_data(excel_file: str) -> list[dict]:
    """
    Reads data from an Excel file and returns a list of dictionaries.

    Args:
        excel_file (str): The path to the Excel file.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary represents a row in the Excel file.
    """
    try:
        df = pd.read_excel(excel_file)

        # Verify if all required columns are present
        required_columns = ['title', 'credit', 'grade']
        if not all(column in df.columns for column in required_columns):
            raise ValueError("Error: Missing required columns in the Excel file.")

        # Verify if there are any missing values
        if df.isnull().values.any():
            raise ValueError("Error: Missing values in the Excel file.")

        # Convert the DataFrame to a list of dictionaries
        course_data = df.to_dict(orient='records')

        return course_data

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: Excel file not found: {excel_file}")
    except Exception as e:
        raise Exception(f"Error reading Excel file: {e}")