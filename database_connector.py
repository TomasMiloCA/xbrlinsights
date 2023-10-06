from supabase_py import create_client
import pandas as pd

# Initialize Supabase client
# Replace the URL and anon_key with your actual Supabase URL and anonymous key
url = "https://gpbtlijqrucwttfniqjj.supabase.co"
anon_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdwYnRsaWpxcnVjd3R0Zm5pcWpqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY1NDAxMTQsImV4cCI6MjAxMjExNjExNH0.ALkx9lRuXB56imebGiaD9X1fGIXv4MC0WA5iH6w6Yxc"
supabase = create_client(url, anon_key)



# Function to fetch all records from the 'XBRL' table
def fetch_all_records():
    response = supabase.table("XBRL").select().execute()
    if response['status_code'] == 200:
        df = pd.DataFrame(response['data'])
        return df

# Function to fetch records based on a specific 'name'
def fetch_by_name(name):
    response = supabase.table("XBRL").select().filter('name', 'eq', name).execute()
    if response['status_code'] == 200:
        df = pd.DataFrame(response['data'])
        return df

    else:
        print(f"Failed to fetch records for name {name}: {response.get('error', 'Unknown error')}")

# Function to fetch records with 'value' greater than a specific amount
def fetch_by_value(value):
    response = supabase.table("XBRL").select().filter('value', 'gt', value).execute()
    if response['status_code'] == 200:
        df = pd.DataFrame(response['data'])
        return df
    else:
        print(f"Failed to fetch records with value greater than {value}: {response.get('error', 'Unknown error')}")

# Function to fetch records with 'date' greater than a specific date
def fetch_by_date(date):
    response = supabase.table("XBRL").select().filter('date', 'gt', date).execute()
    if response['status_code'] == 200:
        df = pd.DataFrame(response['data'])
        return df
    else:
        print(f"Failed to fetch records with date greater than {date}: {response.get('error', 'Unknown error')}")



# Fetching records by name 'MIZUHO FINANCIAL GROUP INC'
fetch_by_name('MIZUHO FINANCIAL GROUP INC')

# Fetching records with date greater than '2021-12-31'
fetch_by_date('2021-12-31')
