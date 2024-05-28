import requests


def main():
    """
    Main function that sends a GET request to the GitHub API.

    Prints the JSON response if the request is successful (status code 200).
    Otherwise, prints an error message.
    """
    url = "https://api.github.com"  # Example API endpoint
    response = requests.get(url)
    if response.status_code == 200:
        print("Success! API data received:")
        print(response.json())  # Print JSON response from the API
    else:
        print("Failed to retrieve data.")


if __name__ == "__main__":
    main()
