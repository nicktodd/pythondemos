from typing import Protocol

class DataSource(Protocol):
    def read(self) -> str:
        ...
    def write(self, data: str) -> None:
        ...

class APIClient:
    def read(self) -> str:
        return "Data from API"

    def write(self, data: str) -> None:
        print(f"Sending data to API: {data}")

class CSVHandler:
    def read(self) -> str:
        return "Data from CSV"

    def write(self, data: str) -> None:
        print(f"Writing to CSV: {data}")

def process_data(source: DataSource) -> None:
    data = source.read()
    print(f"Processing: {data}")
    source.write("Processed data")

api_client = APIClient()
csv_handler = CSVHandler()

process_data(api_client)  # Works with APIClient
process_data(csv_handler)  # Works with CSVHandler