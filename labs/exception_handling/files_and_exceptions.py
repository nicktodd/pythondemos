"""
Exercise 9: Exception Handling with Files

In this lab you will practice exception handling when working with text files
and CSV files. Complete each function by replacing the `pass` statements with
your own implementation.

Run this file directly to test your solutions:
    python files_and_exceptions.py

Sample files provided in this folder:
    sample_text.txt  – plain text file with 10 lines
    sample_data.csv  – CSV with columns: id, name, value
                       (contains intentionally bad rows for Part 3)
"""

import csv
import os


# ---------------------------------------------------------------------------
# PART 1 – Text files
# ---------------------------------------------------------------------------

def read_text_file(filepath: str) -> str:
    """
    Read the entire contents of a text file and return it as a string.

    Handle the following exceptions:
        - FileNotFoundError  : return the string "File not found: <filepath>"
        - PermissionError    : return the string "Permission denied: <filepath>"
        - OSError            : return the string "OS error reading file: <filepath>"

    The file must be closed whether an exception occurs or not (use a
    try/except/finally block OR a 'with' statement).
    """
    pass


def write_text_file(filepath: str, content: str) -> bool:
    """
    Write 'content' to 'filepath', creating it if it does not exist.

    Return True on success, False on failure.

    Handle the following exceptions:
        - PermissionError : print a descriptive message and return False
        - OSError         : print a descriptive message and return False
    """
    pass


def append_to_text_file(filepath: str, line: str) -> bool:
    """
    Append 'line' (followed by a newline) to an existing text file.

    Return True on success, False on failure.

    Handle the following exceptions:
        - FileNotFoundError : print a descriptive message and return False
        - PermissionError   : print a descriptive message and return False
        - OSError           : print a descriptive message and return False
    """
    pass


def count_lines(filepath: str) -> int:
    """
    Return the number of lines in 'filepath'.

    Handle the following exceptions:
        - FileNotFoundError : return -1
        - OSError           : return -1
    """
    pass


# ---------------------------------------------------------------------------
# PART 2 – CSV files
# ---------------------------------------------------------------------------

def read_csv_file(filepath: str) -> list[dict]:
    """
    Read a CSV file that has a header row and return a list of dicts,
    one dict per data row (using csv.DictReader).

    Handle the following exceptions:
        - FileNotFoundError : print a descriptive message and return []
        - PermissionError   : print a descriptive message and return []
        - csv.Error         : print a descriptive message and return []
        - OSError           : print a descriptive message and return []
    """
    pass


def write_csv_file(filepath: str, fieldnames: list[str], rows: list[dict]) -> bool:
    """
    Write 'rows' (a list of dicts) to a CSV file with a header row.

    Use csv.DictWriter with the provided 'fieldnames'.

    Return True on success, False on failure.

    Handle the following exceptions:
        - PermissionError : print a descriptive message and return False
        - csv.Error       : print a descriptive message and return False
        - OSError         : print a descriptive message and return False

    Raise ValueError if 'fieldnames' is empty.
    """
    pass


def get_csv_column(filepath: str, column_name: str) -> list:
    """
    Return a list of all values in 'column_name' from 'filepath'.

    Handle the following exceptions:
        - FileNotFoundError : print a descriptive message and return []
        - KeyError          : print a descriptive message (column not found)
                              and return []
        - csv.Error         : print a descriptive message and return []
        - OSError           : print a descriptive message and return []
    """
    pass


# ---------------------------------------------------------------------------
# PART 3 – Putting it together
# ---------------------------------------------------------------------------

def process_csv_safely(filepath: str, output_filepath: str) -> bool:
    """
    Read a CSV file of numbers with columns 'id' and 'value'.
    Calculate the sum of all 'value' entries (converting each to float).
    Write a new CSV file at 'output_filepath' with columns 'id', 'value',
    and 'squared' (value ** 2).

    Return True on success, False if any unrecoverable error occurs.

    Requirements:
        - Skip any row where 'value' cannot be converted to float (handle
          ValueError) but continue processing the remaining rows.
        - Handle FileNotFoundError, csv.Error, and OSError around file I/O.
        - Print a summary showing how many rows were processed and how many
          were skipped.
    """
    pass


# ---------------------------------------------------------------------------
# Simple smoke-tests – run with: python files_and_exceptions.py
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    SAMPLE_TXT = "sample_text.txt"
    SAMPLE_CSV = "sample_data.csv"
    TEST_TXT = "test_output.txt"
    TEST_CSV = "test_output.csv"
    TEST_PROCESSED = "test_processed.csv"

    print("=== Part 1: Text files ===")

    # read the provided sample file
    content = read_text_file(SAMPLE_TXT)
    print("sample_text.txt contents:\n", content)

    # count lines in the sample file
    print("Line count (sample_text.txt):", count_lines(SAMPLE_TXT))

    # append a new line to a copy so the original stays intact
    write_text_file(TEST_TXT, content)
    append_to_text_file(TEST_TXT, "Appended line")
    print("Line count after append:", count_lines(TEST_TXT))

    # missing file
    result = read_text_file("nonexistent_file.txt")
    print("Missing file result:", result)

    print("\n=== Part 2: CSV files ===")

    # read the provided sample CSV
    rows = read_csv_file(SAMPLE_CSV)
    print("Rows from sample_data.csv:", rows)

    names = get_csv_column(SAMPLE_CSV, "name")
    print("Name column:", names)

    missing_col = get_csv_column(SAMPLE_CSV, "nonexistent")
    print("Missing column result:", missing_col)

    # write a small CSV from scratch
    fieldnames = ["id", "value"]
    sample_rows = [
        {"id": "1", "value": "10.5"},
        {"id": "2", "value": "bad_data"},
        {"id": "3", "value": "30.0"},
        {"id": "4", "value": ""},
    ]
    write_csv_file(TEST_CSV, fieldnames, sample_rows)

    print("\n=== Part 3: Processing ===")
    # process the provided sample_data.csv (has intentionally bad rows)
    process_csv_safely(SAMPLE_CSV, TEST_PROCESSED)
    processed = read_csv_file(TEST_PROCESSED)
    print("Processed rows:", processed)

    # cleanup test files only (leave sample files intact)
    for f in [TEST_TXT, TEST_CSV, TEST_PROCESSED]:
        if os.path.exists(f):
            os.remove(f)

    print("\nDone.")
