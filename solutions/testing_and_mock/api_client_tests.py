"""
API Client Tests Solution

Complete implementation of tests for an API client using mocking techniques.
"""

import pytest
from unittest.mock import Mock, patch
import requests


class APIClient:
    """API client for external service calls."""

    def __init__(self, base_url="https://jsonplaceholder.typicode.com"):
        self.base_url = base_url

    def get_user(self, user_id):
        """Get user data from API."""
        response = requests.get(f"{self.base_url}/users/{user_id}")
        response.raise_for_status()
        return response.json()

    def create_post(self, title, body, user_id):
        """Create a new post."""
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(f"{self.base_url}/posts", json=data)
        response.raise_for_status()
        return response.json()

    def get_weather(self, city):
        """Get weather data for a city."""
        # Simulating a weather API call
        response = requests.get(f"https://api.weather.com/v1/weather/{city}")
        response.raise_for_status()
        return response.json()


@patch('requests.get')
def test_get_user_success(mock_get):
    """Test successful user retrieval."""
    mock_response = Mock()
    mock_response.json.return_value = {"id": 1, "name": "John Doe", "email": "john@example.com"}
    mock_get.return_value = mock_response

    client = APIClient()
    result = client.get_user(1)

    assert result["name"] == "John Doe"
    assert result["email"] == "john@example.com"
    mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users/1")


@patch('requests.get')
def test_get_user_not_found(mock_get):
    """Test user not found scenario."""
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    mock_get.return_value = mock_response

    client = APIClient()
    with pytest.raises(requests.exceptions.HTTPError):
        client.get_user(999)


@patch('requests.get')
def test_get_user_network_error(mock_get):
    """Test network error scenario."""
    mock_get.side_effect = requests.exceptions.ConnectionError("Network error")

    client = APIClient()
    with pytest.raises(requests.exceptions.ConnectionError):
        client.get_user(1)


@patch('requests.post')
def test_create_post_success(mock_post):
    """Test successful post creation."""
    mock_response = Mock()
    mock_response.json.return_value = {"id": 101, "title": "Test Post", "body": "Test body", "userId": 1}
    mock_post.return_value = mock_response

    client = APIClient()
    result = client.create_post("Test Post", "Test body", 1)

    assert result["id"] == 101
    assert result["title"] == "Test Post"
    mock_post.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "Test Post", "body": "Test body", "userId": 1}
    )


@patch('requests.post')
def test_create_post_failure(mock_post):
    """Test post creation failure."""
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("400 Bad Request")
    mock_post.return_value = mock_response

    client = APIClient()
    with pytest.raises(requests.exceptions.HTTPError):
        client.create_post("Test Post", "Test body", 1)


@patch('requests.get')
def test_get_weather_success(mock_get):
    """Test successful weather data retrieval."""
    mock_response = Mock()
    mock_response.json.return_value = {"temperature": 22, "condition": "sunny", "city": "London"}
    mock_get.return_value = mock_response

    client = APIClient()
    result = client.get_weather("London")

    assert result["temperature"] == 22
    assert result["condition"] == "sunny"
    mock_get.assert_called_once_with("https://api.weather.com/v1/weather/London")


@patch('requests.get')
@patch('requests.post')
def test_api_client_with_custom_mock(mock_post, mock_get):
    """Test API client with custom mock responses."""
    # Setup get mock
    get_response = Mock()
    get_response.json.return_value = {"id": 2, "name": "Jane Doe"}
    mock_get.return_value = get_response

    # Setup post mock
    post_response = Mock()
    post_response.json.return_value = {"id": 102, "title": "Custom Post"}
    mock_post.return_value = post_response

    client = APIClient()

    # Test get_user
    user = client.get_user(2)
    assert user["name"] == "Jane Doe"

    # Test create_post
    post = client.create_post("Custom Post", "Custom body", 2)
    assert post["id"] == 102

    # Verify calls
    assert mock_get.call_count == 1
    assert mock_post.call_count == 1


@patch('requests.post')
def test_api_call_verification(mock_post):
    """Test that correct API calls are made."""
    mock_response = Mock()
    mock_response.json.return_value = {"id": 103}
    mock_post.return_value = mock_response

    client = APIClient("https://custom-api.com")

    result = client.create_post("Verify Call", "Verify body", 5)

    # Verify the call was made with correct parameters
    mock_post.assert_called_once_with(
        "https://custom-api.com/posts",
        json={
            "title": "Verify Call",
            "body": "Verify body",
            "userId": 5
        }
    )

    # Verify the response was processed
    assert result["id"] == 103


@patch('requests.get')
def test_multiple_api_calls(mock_get):
    """Test multiple API calls in sequence."""
    mock_responses = [
        Mock(json=lambda: {"id": 1, "name": "User 1"}),
        Mock(json=lambda: {"id": 2, "name": "User 2"}),
        Mock(json=lambda: {"temperature": 25, "city": "Paris"})
    ]
    mock_get.side_effect = mock_responses

    client = APIClient()

    # Multiple calls
    user1 = client.get_user(1)
    user2 = client.get_user(2)
    weather = client.get_weather("Paris")

    assert user1["name"] == "User 1"
    assert user2["name"] == "User 2"
    assert weather["temperature"] == 25

    # Verify all calls were made
    assert mock_get.call_count == 3
