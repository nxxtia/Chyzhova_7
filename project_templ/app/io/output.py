import pandas as pd


def output_text_to_console(text):
    """
    Outputs text to the console.

    Args:
        text (str): Text to output.
    """
    print(text)


def write_to_file(filename, content):
    """
    Writes text to a file using Python's built-in capabilities.

    Args:
        filename (str): The path to the file to write the text to.
        content (str): Text to record.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def write_to_file_with_pandas(filename, data):
    """
    Writes data to a CSV file using the pandas library.

    Args:
        filename (str): The path to the file to be written to.
        data (DataFrame): The data in DataFrame format to be written.
    """
    data.to_csv(filename, index=False, encoding='utf-8')
