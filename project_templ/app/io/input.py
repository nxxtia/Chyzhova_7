import pandas as pd


def input_text_from_console():
    """
    Запитує текст у користувача та повертає його.
    """
    return input("Будь ласка, введіть текст: ")


def read_from_file(filename):
    """
    Читає вміст файлу за допомогою вбудованих можливостей Python.

    Args:
        filename (str): Шлях до файлу, який потрібно прочитати.

    Returns:
        str: Вміст файлу.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def read_from_file_with_pandas(filename):
    """
    Читає вміст файлу за допомогою бібліотеки Pandas.

    Args:
        filename (str): Шлях до файлу, який потрібно прочитати.

    Returns:
        DataFrame: Вміст файлу у формі DataFrame.
    """
    return pd.read_csv(filename, encoding='utf-8')

