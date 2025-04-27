import requests
import os

def load_remote_csv():
    """
    Downloads a CSV file from a remote URL and saves it to a temporary location.
    
    Returns:
        None
    Raises:
        requests.RequestException: If the download fails.
    """
    # URL of the remote CSV file (replace with actual URL)
    url = "https://github.com/batchayw/tech-data-analysis/blob/main/broadband_data_zipcode.csv"
    
    # Send a GET request to download the file
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        print(f"Failed to download CSV: {e}")
        raise
    
    # Ensure the /tmp directory exists
    os.makedirs("/tmp", exist_ok=True)
    
    # Save the file to /tmp/remote_data.csv
    with open("/tmp/remote_data.csv", "wb") as f:
        f.write(response.content)
    print("CSV file downloaded successfully to /tmp/remote_data.csv")

if __name__ == "__main__":
    load_remote_csv()