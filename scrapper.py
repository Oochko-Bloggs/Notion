import requests
import re
from bs4 import BeautifulSoup
from notion_client import Client 
from datetime import datetime
from dateutil import parser


start_date = None
end_date = None

# URL of the Pley.gg website and your notion api
URL = "https://pley.gg/cs2-tournament-calendar/"
notion = Client(auth="")

database_id = "https://www.notion.so/1c2a7d326ccf8054b7e9e4f79cfab4a6?v=1c2a7d326ccf80639211000c5f0cc711"
# Set a custom User-Agent (important to prevent being blocked)
HEADERS = {
    "User-Agent": "NotionCS2Tracker/1.0"
}

def extract_datetime(details):
	match = re.search(r'(\w+\s\d{1,2}[a-z]{2})\s–\s(\w+\s\d{1,2}[a-z]{2})', details)
	if match:
		start_date_str = match.group(1)
		end_date_str = match.group(2)
		return start_date_str, end_date_str
	return None, None


def convert_to_standard_date(date_str):
    # Remove the suffix
    date_str = re.sub(r'(st|nd|rd|th)', '', date_str)
    # Parse the date string into a datetime object
    return parser.parse(date_str)


# Send GET request to the webpage
response = requests.get(URL, headers=HEADERS)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

   
    event_headers = soup.find_all("h2")

    event_name = None 
    event_details = []

    # Loop through each <h2> header
    for header in event_headers:
        
        event_name = header.find('strong')
        event_details.append(header.text.strip())


        """
        name = event_card.find_next_sibling()
        next_element = event_card.find_next_sibling()
        while next_element and next_element.name == "p" and ":" in next_element.text.strip() and ":" in next_element.name.text.strip():
        	line = next_element.text.strip()
        	event_details.append(line)
	       	if 'Date'in line or 'date' in line:
        		start_date_str, end_date_str = extract_datetime(line)
        		if start_date_str and end_date_str:
        			start_date = convert_to_standard_date(start_date_str).date()
        			end_date = convert_to_standard_date(end_date_str).date()
            next_element = next_element.find_next_sibling()
        event_details_text = "\n".join(event_details)
        #Prepare event data for notion

        event_data = {
        	'parent':{"database_id": database_id},
        	'properties': {
        		'Name': {
        			"title": [
        				{
        					"text":{
        						"content": event_name
        					}
        				}
        			]
        		},
        		'Date': {
        			'date': {
        				'start': datetime.now().isoformat()
        			}
        		},
        		'Details': {
        			'rich_text': [
        				{
        					'text':{
        						'content': "\n".join(event_details)
        					}
        				}
        			]
        		}
        	}
        }

        #add the event to the Notion calendar

        notion.pages.create(**event_data)
"""
        #print(f'Added event: {event_name}')
        # Print the extracted event data
        print(f"🔹 Event: {event_name}")
#        print("\n".join(event_details))
  
        print("=" * 50)  # Separator for readability

else:
    print(f"Failed to fetch the page. Status Code: {response.status_code}")
