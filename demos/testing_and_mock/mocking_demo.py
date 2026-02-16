# filepath: d:\GitRepos\Courses\pythondemos\demos\testing_and_mock\mocking_demo.py
"""
Mocking Demo

This module demonstrates mocking techniques in pytest:
- unittest.mock usage
- Mock objects and MagicMock
- Patching functions and methods
- Mock side effects
- Assertions on mocks
- pytest-mock integration
"""

import pytest
from unittest.mock import Mock, MagicMock, patch, MagicMock, call
import requests
import json
import os
import time


# Sample application code to test
class WeatherAPI:
    """Weather API client."""

    def __init__(self, api_key=None):
        self.api_key = api_key or "default_key"
        self.base_url = "https://api.weather.com"

    def get_weather(self, city):
        """Get weather data for a city."""
        url = f"{self.base_url}/weather/{city}"
        params = {"apikey": self.api_key}

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()

    def get_forecast(self, city, days=3):
        """Get weather forecast for a city."""
        url = f"{self.base_url}/forecast/{city}"
        params = {"apikey": self.api_key, "days": days}

        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()


class DataProcessor:
    """Class that processes data from external sources."""

    def __init__(self, api_client=None):
        self.api_client = api_client

    def process_weather_data(self, city):
        """Process weather data for a city."""
        try:
            data = self.api_client.get_weather(city)
            temp = data.get("temperature", 0)
            condition = data.get("condition", "unknown")

            # Process temperature
            if temp > 30:
                status = "hot"
            elif temp < 10:
                status = "cold"
            else:
                status = "moderate"

            return {
                "city": city,
                "temperature": temp,
                "condition": condition,
                "status": status
            }
        except Exception as e:
            return {"error": str(e)}

    def save_to_file(self, data, filename):
        """Save data to a file."""
        with open(filename, 'w') as f:
            json.dump(data, f)
        return True

    def load_from_file(self, filename):
        """Load data from a file."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} not found")
        with open(filename, 'r') as f:
            return json.load(f)


class EmailService:
    """Service for sending emails."""

    def __init__(self, smtp_server="smtp.gmail.com"):
        self.smtp_server = smtp_server

    def send_email(self, to_email, subject, body):
        """Send an email (simplified)."""
        # In real implementation, this would connect to SMTP server
        print(f"Sending email to {to_email}")
        print(f"Subject: {subject}")
        print(f"Body: {body}")
        return True

    def send_bulk_emails(self, emails, subject, body):
        """Send emails to multiple recipients."""
        results = []
        for email in emails:
            result = self.send_email(email, subject, body)
            results.append(result)
        return results


# Basic Mock usage
def test_weather_api_with_mock():
    """Test WeatherAPI with a basic mock."""
    # Create a mock response
    mock_response = Mock()
    mock_response.json.return_value = {"temperature": 25, "condition": "sunny"}

    # Create mock for requests.get
    with patch('requests.get') as mock_get:
        mock_get.return_value = mock_response

        api = WeatherAPI()
        result = api.get_weather("London")

        assert result["temperature"] == 25
        assert result["condition"] == "sunny"

        # Verify the mock was called correctly
        mock_get.assert_called_once_with(
            "https://api.weather.com/weather/London",
            params={"apikey": "default_key"}
        )


def test_weather_api_with_magic_mock():
    """Test WeatherAPI with MagicMock."""
    # MagicMock can handle more complex scenarios
    mock_response = MagicMock()
    mock_response.json.return_value = {"temperature": 20, "condition": "cloudy"}
    mock_response.raise_for_status.return_value = None

    with patch('requests.get', return_value=mock_response) as mock_get:
        api = WeatherAPI("test_key")
        result = api.get_forecast("Paris", days=5)

        assert result["temperature"] == 20
        assert result["condition"] == "cloudy"

        # Check call arguments
        args, kwargs = mock_get.call_args
        assert kwargs["params"]["apikey"] == "test_key"
        assert kwargs["params"]["days"] == 5


def test_data_processor_with_mocked_api():
    """Test DataProcessor with mocked API client."""
    # Create mock API client
    mock_api = Mock()
    mock_api.get_weather.return_value = {
        "temperature": 35,
        "condition": "sunny"
    }

    processor = DataProcessor(mock_api)
    result = processor.process_weather_data("Miami")

    assert result["city"] == "Miami"
    assert result["status"] == "hot"
    assert result["temperature"] == 35

    # Verify the API was called
    mock_api.get_weather.assert_called_once_with("Miami")


def test_data_processor_api_error():
    """Test DataProcessor when API raises an error."""
    mock_api = Mock()
    mock_api.get_weather.side_effect = Exception("API Error")

    processor = DataProcessor(mock_api)
    result = processor.process_weather_data("TestCity")

    assert "error" in result
    assert "API Error" in result["error"]


def test_file_operations_with_mocking():
    """Test file operations with mocked open and os.path.exists."""
    processor = DataProcessor()

    test_data = {"test": "data"}

    # Mock open function and json.dump
    with patch('builtins.open', create=True) as mock_open, \
         patch('json.dump') as mock_dump:
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file

        result = processor.save_to_file(test_data, "test.json")

        assert result is True
        # Verify json.dump was called
        mock_dump.assert_called_once_with(test_data, mock_file)


def test_load_from_file_with_mocking():
    """Test loading from file with mocking."""
    processor = DataProcessor()

    with patch('os.path.exists', return_value=True), \
         patch('builtins.open', create=True) as mock_open:

        mock_file = MagicMock()
        mock_file.__enter__.return_value = mock_file
        mock_open.return_value = mock_file

        # Mock json.load
        with patch('json.load', return_value={"loaded": "data"}) as mock_json_load:
            result = processor.load_from_file("test.json")

            assert result["loaded"] == "data"
            mock_json_load.assert_called_once_with(mock_file)


def test_load_from_file_not_found():
    """Test loading from non-existent file."""
    processor = DataProcessor()

    with patch('os.path.exists', return_value=False):
        with pytest.raises(FileNotFoundError):
            processor.load_from_file("nonexistent.json")


def test_email_service_with_mocking():
    """Test EmailService with mocked send_email."""
    service = EmailService()

    with patch.object(service, 'send_email', return_value=True) as mock_send:
        result = service.send_bulk_emails(
            ["user1@test.com", "user2@test.com"],
            "Test Subject",
            "Test Body"
        )

        assert result == [True, True]

        # Verify send_email was called twice with correct arguments
        assert mock_send.call_count == 2
        mock_send.assert_has_calls([
            call("user1@test.com", "Test Subject", "Test Body"),
            call("user2@test.com", "Test Subject", "Test Body")
        ])


def test_email_service_with_side_effects():
    """Test EmailService with side effects on mock."""
    service = EmailService()

    # Mock with side effect that returns different values
    with patch.object(service, 'send_email') as mock_send:
        mock_send.side_effect = [True, False, True]

        result = service.send_bulk_emails(
            ["a@test.com", "b@test.com", "c@test.com"],
            "Subject",
            "Body"
        )

        assert result == [True, False, True]


def test_weather_api_with_different_responses():
    """Test WeatherAPI with different mock responses."""
    api = WeatherAPI()

    # Mock responses for different calls
    responses = [
        Mock(json=lambda: {"temperature": 15, "condition": "rainy"}),
        Mock(json=lambda: {"temperature": 28, "condition": "sunny"}),
    ]

    with patch('requests.get', side_effect=responses) as mock_get:
        # First call
        result1 = api.get_weather("London")
        assert result1["condition"] == "rainy"

        # Second call
        result2 = api.get_weather("Madrid")
        assert result2["condition"] == "sunny"

        assert mock_get.call_count == 2


def test_mock_configuration():
    """Demonstrate various mock configuration options."""
    # Create a mock with default return value
    mock_func = Mock(return_value="default")
    assert mock_func() == "default"

    # Configure different return values for different calls
    mock_func.side_effect = ["first", "second", ValueError("error")]
    assert mock_func() == "first"
    assert mock_func() == "second"
    with pytest.raises(ValueError):
        mock_func()

    # Reset mock
    mock_func.reset_mock()
    assert mock_func.call_count == 0


def test_mock_assertions():
    """Demonstrate mock assertion methods."""
    mock_obj = Mock()

    # Call the mock
    mock_obj.method("arg1", "arg2", kwarg1="value1")

    # Various assertions
    mock_obj.method.assert_called()
    mock_obj.method.assert_called_once()
    mock_obj.method.assert_called_with("arg1", "arg2", kwarg1="value1")
    mock_obj.method.assert_called_once_with("arg1", "arg2", kwarg1="value1")

    # Check call count
    assert mock_obj.method.call_count == 1

    # Check call arguments
    args, kwargs = mock_obj.method.call_args
    assert args == ("arg1", "arg2")
    assert kwargs == {"kwarg1": "value1"}


# Using pytest-mock (if available)
def test_with_pytest_mock(mocker):
    """Test using pytest-mock fixture."""
    # Mock a function
    mock_func = mocker.Mock(return_value="mocked")
    assert mock_func() == "mocked"

    # Patch a module function
    mock_requests = mocker.patch('requests.get')
    mock_requests.return_value.json.return_value = {"data": "test"}

    api = WeatherAPI()
    result = api.get_weather("Test")
    assert result["data"] == "test"


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v"])
