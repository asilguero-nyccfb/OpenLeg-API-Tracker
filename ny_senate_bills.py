import requests
import pandas as pd
import xlsxwriter
from datetime import datetime

# Base URL for API
base_url = 'https://legislation.nysenate.gov/api/3/bills/2024'

# Replace with your actual API key
api_key = "XLC9cIQDZOgmCiMCT43D1umf6VeOFuGU"

def fetch_bill_details(api_key):
    url = f"{base_url}?key={api_key}"
    headers = {'Authorization': f'Token {api_key}'}  # API key in headers if needed

    try:
        response = requests.get(url, headers=headers)

        # Debugging output: print the entire response (in a readable format)
        print(f"Response Data: {response.json()}")  # Print the response as a JSON

        # Raise for HTTP errors
        response.raise_for_status()

        # Return the JSON data if request is successful
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error getting data: {e}")
        return None

#def filter_bill_data (bill_data)

def export_to_excel(bill_data, filename_prefix="NY_Senate_Bills_data"):
    # Generate a timestamp to append to the filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.xlsx"  # Format: NY_Senate_Bills_data_YYYYMMDD_HHMMSS.xlsx

    # Check if 'result' and 'items' exist in the response data
    if 'result' in bill_data and 'items' in bill_data['result']:
        items = bill_data['result']['items']  # Extract the list from result.items

        # Convert the list of items to a DataFrame
        df = pd.DataFrame(items)

        print(f"DataFrame created with shape: {df.shape}")  # Debugging output

        # Export DataFrame to Excel using XlsxWriter engine
        if not df.empty:
            with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Bills')
                print(f"Data has been exported to {filename}")
        else:
            print("No data to export to Excel.")
    else:
        print("'result.items' not found in the API response.")


#Fetch bill details
#bill_data = fetch_bill_details(api_key)

#if bill_data:
    # Print the entire structure of the response for debugging
 #   print(f"Full Response: {bill_data}")

    # Export data to Excel with a timestamped filename
  #  export_to_excel(bill_data)

#else:
 #   print("No data retrieved from the API.")"
