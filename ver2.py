import requests
from bs4 import BeautifulSoup

# URL of the CS2 tournaments page on Pley.gg
URL = "https://pley.gg/cs2-tournament-calendar/"

# Send GET request with User-Agent
response = requests.get(URL, headers={"User-Agent": "NotionCS2Tracker/1.0"})

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    events = []
    current_event = None

    # Iterate through all elements: <h2> for months, <p> for events
    for element in soup.find_all(["h2", "p"]):
        if element.name == "h2":
            # Skip <h2> because it's just a month name
            continue
        
        strong_tag = element.find("strong")  # Check if <p> has <strong> (Event Name)
        
        if strong_tag:
            # If we found a new event, save the previous one
            if current_event:
                events.append(current_event)

            # Start a new event entry
            current_event = {
                "event_name": strong_tag.text.strip(),
                "event_details": []
            }
        else:
            # If it's a normal <p> and an event exists, add details
            if current_event:
                current_event["event_details"].append(element.text.strip())

    # Add the last event after finishing the loop
    if current_event:
        events.append(current_event)

    # Print extracted events
    for event in events:
        print("Event Name:", event["event_name"])
        print("Event Details:", ", ".join(event["event_details"]))
        print("-" * 30)

else:
    print(f"Failed to fetch the page. Status Code: {response.status_code}")
