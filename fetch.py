import requests
import json
import pandas as pd
import requests


# Wikipedia API endpoint
ENDPOINT = 'https://en.wikipedia.org/w/api.php'

# Parameters for the API query, requesting the revision history of the "Climate Change" page
parameters = {
    'action': 'query',
    'format': 'json',
    'titles': 'Climate_change',
    'prop': 'revisions',
    'rvlimit': 50,  # Fetch the last 50 revisions
    'rvprop': 'ids|timestamp|user|comment|size'  # Information you want about the revisions
}

def get_revision_history():
    # Make a request to the Wikipedia API
    response = requests.get(ENDPOINT, params=parameters)
    
    # Parse the response in JSON format
    data = response.json()
    
    # Extract the pages from the JSON
    pages = data['query']['pages']
    
    # Iterate through all pages (there should only be one in this case)
    for page_id in pages:
        page = pages[page_id]
        print(f"Title: {page['title']}, Page ID: {page_id}")
        revisions = page.get('revisions', [])
        for rev in revisions:
            print(f"Revision ID: {rev['revid']}, User: {rev['user']}, Timestamp: {rev['timestamp']}, Comment: {rev['comment']}, Size: {rev['size']}")



# ... [Previous code remains the same] ...

def get_revision_history():
    response = requests.get(ENDPOINT, params=parameters)
    data = response.json()

    # Extracting revisions and converting them into a DataFrame
    pages = data['query']['pages']
    for page_id in pages:
        revisions = pages[page_id].get('revisions', [])
        df = pd.DataFrame(revisions)
        return df  # Return the DataFrame instead of printing

# Fetch data
revision_data = get_revision_history()

# Print first few rows of the DataFrame
print(revision_data.head())


import matplotlib.pyplot as plt

# Convert timestamp to datetime and set it as the index
revision_data['timestamp'] = pd.to_datetime(revision_data['timestamp'])
revision_data.set_index('timestamp', inplace=True)

# Resampling data by month and counting the number of edits
monthly_edits = revision_data.resample('M').size()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(monthly_edits, marker='o', linestyle='-', color='b')
plt.title('Number of Edits per Month')
plt.xlabel('Month')
plt.ylabel('Number of Edits')
plt.grid(True)
plt.show()


top_contributors = revision_data['user'].value_counts().head(10)  # Top 10 contributors

plt.figure(figsize=(12, 6))
top_contributors.plot(kind='bar', color='skyblue')
plt.title('Top 10 Contributors')
plt.xlabel('User')
plt.ylabel('Number of Contributions')
plt.xticks(rotation=45)
plt.show()
