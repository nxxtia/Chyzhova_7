import pandas as pd
from app.io.output import output_text_to_console, write_to_file, write_to_file_with_pandas
from app.io.input import input_text_from_console, read_from_file, read_from_file_with_pandas


def main():
    text_from_console = input_text_from_console()
    output_text_to_console(text_from_console)

    filename = "data/test_output.txt"
    write_to_file(filename, text_from_console)

    file_content = read_from_file(filename)
    output_text_to_console(f"File contents {filename}:\n{file_content}")

    csv_filename = "data/test.csv"
    df = read_from_file_with_pandas(csv_filename)
    output_text_to_console(f"DataFrame read from {csv_filename}:\n{df}")

    if isinstance(df, pd.DataFrame):
        write_to_file_with_pandas('data/new_test_output.csv', df)
    else:
        print("Error: The data passed is not a DataFrame object.")


if __name__ == "__main__":
    main()
    