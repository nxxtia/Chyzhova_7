import pandas as pd


def output_text_to_console(text):
    """
    Виводить текст у консоль.

    Args:
        text (str): Текст для виводу.
    """
    print(text)


def write_to_file(filename, content):
    """
    Записує текст до файлу за допомогою вбудованих можливостей Python.

    Args:
        filename (str): Шлях до файлу, в який потрібно записати текст.
        content (str): Текст для запису.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)


def write_to_file_with_pandas(filename, data):
    """
    Записує дані до файлу у форматі CSV за допомогою бібліотеки pandas.

    Args:
        filename (str): Шлях до файлу, у який буде здійснено запис.
        data (DataFrame): Дані у форматі DataFrame, які потрібно записати.
    """
    data.to_csv(filename, index=False, encoding='utf-8')
