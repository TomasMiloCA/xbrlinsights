from supabase_py import create_client

# Initialize Supabase client
# Replace the URL and anon_key with your actual Supabase URL and anonymous key
url = "https://gpbtlijqrucwttfniqjj.supabase.co"
anon_key = "insert anon key here"
supabase = create_client(url, anon_key)

# Function to fetch all records from the 'XBRL' table
def fetch_all_records():
    response = supabase.table("XBRL").select().execute()
    if response['status_code'] == 200:
        print("All records fetched successfully.")
        print(response['data'])
    else:
        print(f"Failed to fetch all records: {response.get('error', 'Unknown error')}")

# Function to fetch records based on a specific 'name'
def fetch_by_name(name):
    response = supabase.table("XBRL").select().filter('name', 'eq', name).execute()
    if response['status_code'] == 200:
        print(f"Records for name {name} fetched successfully.")
        print(response['data'])
    else:
        print(f"Failed to fetch records for name {name}: {response.get('error', 'Unknown error')}")

# Function to fetch records with 'value' greater than a specific amount
def fetch_by_value(value):
    response = supabase.table("XBRL").select().filter('value', 'gt', value).execute()
    if response['status_code'] == 200:
        print(f"Records with value greater than {value} fetched successfully.")
        print(response['data'])
    else:
        print(f"Failed to fetch records with value greater than {value}: {response.get('error', 'Unknown error')}")

# Function to fetch records with 'date' greater than a specific date
def fetch_by_date(date):
    response = supabase.table("XBRL").select().filter('date', 'gt', date).execute()
    if response['status_code'] == 200:
        print(f"Records with date greater than {date} fetched successfully.")
        print(response['data'])
    else:
        print(f"Failed to fetch records with date greater than {date}: {response.get('error', 'Unknown error')}")



# Fetching records by name 'MIZUHO FINANCIAL GROUP INC'
fetch_by_name('MIZUHO FINANCIAL GROUP INC')

# Fetching records with value greater than 10000000000
fetch_by_value(10000000000)

# Fetching records with date greater than '2021-12-31'
fetch_by_date('2021-12-31')

