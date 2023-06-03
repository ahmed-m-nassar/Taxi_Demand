import requests
from datetime import datetime, timedelta

def download_yellow_taxi_data(start_date, end_date):
    base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/"

    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    while current_date <= end_date:
        file_name = f"yellow_tripdata_{current_date.strftime('%Y-%m')}.parquet"
        url = f"{base_url}{file_name}"

        response = requests.get(url)

        if response.status_code == 200:
            with open(file_name, "wb") as f:
                f.write(response.content)
            print(f"{file_name} downloaded successfully.")
        else:
            print(f"Failed to download {url}.")

        # Move to the next month
        current_date = current_date + timedelta(days=31)  # Assuming each month has 31 days for simplicity

# Example usage
start_date = "2023-01-01"
end_date = "2023-02-01"
download_yellow_taxi_data(start_date, end_date)
