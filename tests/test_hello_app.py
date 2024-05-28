from unittest.mock import patch

import requests

from src.hello_app.hello_main import main


def test_main_success(capsys):
    """
    Test case for successful API request.

    Mocks the requests.get() function to return a response with status code 200
    and checks if the expected output is printed.
    """
    with patch.object(requests, "get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"message": "Hello, World!"}

        main()

        captured = capsys.readouterr()
        assert "Success! API data received:" in captured.out
        assert "{'message': 'Hello, World!'}" in captured.out


def test_main_failure(capsys):
    """
    Test case for failed API request.

    Mocks the requests.get() function to return a response with status code 404
    and checks if the expected error message is printed.
    """
    with patch.object(requests, "get") as mock_get:
        mock_get.return_value.status_code = 404

        main()

        captured = capsys.readouterr()
        assert "Failed to retrieve data." in captured.out
