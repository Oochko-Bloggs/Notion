import requests
from bs4 import BeautifulSoup

# URL of the CS2 tournaments page on Liquipedia
URL = "https://pley.gg/cs2-tournament-calendar/"

# Send GET request to the webpage
response = requests.get(URL, headers={"User-Agent": "NotionCS2Tracker/1.0 (your-email@example.com)"})

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all <p> tags
    all_paragraphs = soup.find_all("p")

    # Initialize a flag to track when we're reading details for an event
    event_name = None
    event_details = []

    # Loop through all <p> tags
    for paragraph in all_paragraphs:
        # Check if the <p> tag contains a <strong> tag (which holds the event name)
        event_name_tag = paragraph.find("strong")
        
        if event_name_tag:
            # If event_name_tag is found, it means this <p> tag contains the event name
            if event_name:  # If we already have an event name, process the previous event
                # Now you have both event_name and event_details for the last event
                print(f"Event Name: {event_name}")
                print(f"Event Details: {event_details}")
                print("-" * 30)  # Separator between events
            # Set the new event name
            event_name = event_name_tag.text.strip()
            event_details = []  # Reset event details list for the new event
        else:
            # Collect details for the current event
            event_details.append(paragraph.text.strip())

    # After the loop, we should print the last event details
#    if event_name and event_details:
#        print(f"Event Name: {event_name}")
#        for details in event_details : print(f"\n{details}")
else:
    print(f"Failed to fetch the page. Status Code: {response.status_code}")
