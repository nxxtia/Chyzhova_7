import pandas as pd


def input_text_from_console():
    """
    Requests text from the user and returns it.
    """
    return input("Please enter the text: ")


def read_from_file(filename):
    """
    Reads the contents of a file using Python's built-in capabilities.

    Args:
        filename (str): The path to the file to read.

    Returns:
        str: File content.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def read_from_file_with_pandas(filename):
    """
    Reads the contents of a file using the Pandas library.

    Args:
        filename (str): The path to the file to read.

    Returns:
        DataFrame: The contents of a file in the form of a DataFrame.
    """
    try:
        return pd.read_csv(filename, encoding='utf-8')
    except pd.errors.EmptyDataError:
        return pd.DataFrame()

