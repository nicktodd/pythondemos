"""
Exercise 9: Exception Handling with Files — SOLUTION

Sample files used (copy from labs/exception_handling/):
    sample_text.txt  – plain text file with 10 lines
    sample_data.csv  – CSV with columns: id, name, value
                       (contains intentionally bad rows for Part 3)

Run this file directly to verify the solutions:
    python files_and_exceptions.py
"""

import csv
import os


# ---------------------------------------------------------------------------
# PART 1 – Text files
# ---------------------------------------------------------------------------

def read_text_file(filepath: str) -> str:
    """Read the entire contents of a text file and return it as a string."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"File not found: {filepath}"
    except PermissionError:
        return f"Permission denied: {filepath}"
    except OSError:
        return f"OS error reading file: {filepath}"


def write_text_file(filepath: str, content: str) -> bool:
    """Write 'content' to 'filepath', creating it if it does not exist."""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except PermissionError:
        print(f"Permission denied: cannot write to {filepath}")
        return False
    except OSError as e:
        print(f"OS error writing to {filepath}: {e}")
        return False


def append_to_text_file(filepath: str, line: str) -> bool:
    """Append 'line' (followed by a newline) to an existing text file."""
    try:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(line + "\n")
        return True
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return False
    except PermissionError:
        print(f"Permission denied: cannot append to {filepath}")
        return False
    except OSError as e:
        print(f"OS error appending to {filepath}: {e}")
        return False


def count_lines(filepath: str) -> int:
    """Return the number of lines in 'filepath'."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        return -1
    except OSError:
        return -1


# ---------------------------------------------------------------------------
# PART 2 – CSV files
# ---------------------------------------------------------------------------

def read_csv_file(filepath: str) -> list[dict]:
    """Read a CSV file with a header row into a list of dicts."""
    try:
        with open(filepath, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []
    except PermissionError:
        print(f"Permission denied: {filepath}")
        return []
    except csv.Error as e:
        print(f"CSV error reading {filepath}: {e}")
        return []
    except OSError as e:
        print(f"OS error reading {filepath}: {e}")
        return []


def write_csv_file(filepath: str, fieldnames: list[str], rows: list[dict]) -> bool:
    """Write 'rows' to a CSV file with a header row."""
    if not fieldnames:
        raise ValueError("fieldnames must not be empty")
    try:
        with open(filepath, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        return True
    except PermissionError:
        print(f"Permission denied: cannot write to {filepath}")
        return False
    except csv.Error as e:
        print(f"CSV error writing to {filepath}: {e}")
        return False
    except OSError as e:
        print(f"OS error writing to {filepath}: {e}")
        return False


def get_csv_column(filepath: str, column_name: str) -> list:
    """Return a list of all values in 'column_name' from 'filepath'."""
    try:
        with open(filepath, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        # Validate the column exists
        if rows and column_name not in rows[0]:
            raise KeyError(column_name)
        return [row[column_name] for row in rows]
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return []
    except KeyError:
        print(f"Column not found: '{column_name}' does not exist in {filepath}")
        return []
    except csv.Error as e:
        print(f"CSV error reading {filepath}: {e}")
        return []
    except OSError as e:
        print(f"OS error reading {filepath}: {e}")
        return []


# ---------------------------------------------------------------------------
# PART 3 – Putting it together
# ---------------------------------------------------------------------------

def process_csv_safely(filepath: str, output_filepath: str) -> bool:
    """
    Read a CSV file with 'id', 'name' (optional), and 'value' columns.
    Skip rows where 'value' cannot be converted to float.
    Write a new CSV with a 'squared' column added.
    Print a summary of processed vs skipped rows.
    """
    try:
        rows = read_csv_file(filepath)
        if not rows:
            print("No data to process.")
            return False
    except Exception as e:
        print(f"Failed to read {filepath}: {e}")
        return False

    processed = []
    skipped = 0

    for row in rows:
        try:
            value = float(row["value"])
            processed.append({**row, "squared": value ** 2})
        except (ValueError, KeyError):
            print(f"Skipping row with invalid value: {row}")
            skipped += 1

    print(f"Processed: {len(processed)} rows, Skipped: {skipped} rows")

    if not processed:
        print("No valid rows to write.")
        return False

    output_fieldnames = list(processed[0].keys())
    return write_csv_file(output_filepath, output_fieldnames, processed)


# ---------------------------------------------------------------------------
# Smoke-tests – run with: python files_and_exceptions.py
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    SAMPLE_TXT = "sample_text.txt"
    SAMPLE_CSV = "sample_data.csv"
    TEST_TXT = "test_output.txt"
    TEST_CSV = "test_output.csv"
    TEST_PROCESSED = "test_processed.csv"

    print("=== Part 1: Text files ===")

    content = read_text_file(SAMPLE_TXT)
    print("sample_text.txt contents:\n", content)

    print("Line count (sample_text.txt):", count_lines(SAMPLE_TXT))

    write_text_file(TEST_TXT, content)
    append_to_text_file(TEST_TXT, "Appended line")
    print("Line count after append:", count_lines(TEST_TXT))

    result = read_text_file("nonexistent_file.txt")
    print("Missing file result:", result)

    print("\n=== Part 2: CSV files ===")

    rows = read_csv_file(SAMPLE_CSV)
    print("Rows from sample_data.csv:", rows)

    names = get_csv_column(SAMPLE_CSV, "name")
    print("Name column:", names)

    missing_col = get_csv_column(SAMPLE_CSV, "nonexistent")
    print("Missing column result:", missing_col)

    fieldnames = ["id", "value"]
    sample_rows = [
        {"id": "1", "value": "10.5"},
        {"id": "2", "value": "bad_data"},
        {"id": "3", "value": "30.0"},
        {"id": "4", "value": ""},
    ]
    write_csv_file(TEST_CSV, fieldnames, sample_rows)

    print("\n=== Part 3: Processing ===")
    process_csv_safely(SAMPLE_CSV, TEST_PROCESSED)
    processed = read_csv_file(TEST_PROCESSED)
    print("Processed rows:", processed)

    for f in [TEST_TXT, TEST_CSV, TEST_PROCESSED]:
        if os.path.exists(f):
            os.remove(f)

    print("\nDone.")
