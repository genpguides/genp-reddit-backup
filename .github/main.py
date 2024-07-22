import requests
import json
from pathlib import Path
import time
import urllib.parse

# Helper functions
def create_file(content, file_path):
    # If directory in the file path does not exist, create the directory
    print("Creating File: " + file_path)
    file_path = Path(file_path)
    directory = file_path.parents[0]
    Path.mkdir(directory, parents=True, exist_ok=True)
    with open(str(file_path), 'w') as f:
        f.write(content)

def save_to_wayback(url):
    wayback_url = f'https://web.archive.org/save/{url}'
    data = {
        'url': urllib.parse.quote_plus(url),
        'capture_all': 'on'
    }
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        response = requests.post(wayback_url, data=data, headers=headers)
        print(f"Sending request to: {wayback_url}")
        print(f"Received Response: {response.status_code} {response.text[:100]}")
        return response.status_code, response.text
    except:
        print(f"Some error occurred while saving {url}")
        return None        


def get_wayback_content(url):
    # Strip 'https://www.' from the beginning of the URL if present
    # Construct the Wayback Machine API URL
    api_url = f'https://web.archive.org/web/{url}'
    try:
        # Make the initial request to the Wayback Machine API
        print(f"Getting Content from {api_url}")
        response = requests.get(api_url)
        return response
    except:
        # Return None if any error occurred or if the content couldn't be retrieved
        return None

def get_response(url):
    print(f"Saving {url}")
    save_to_wayback(url)
    print("Sleeping")
    time.sleep(3)
    return get_wayback_content(url)
    
# Downloading Functions
def get_wiki_pages_names():
    url = 'https://www.reddit.com/r/genp/wiki/pages.json'
    # headers = {'User-Agent': 'Mozilla/5.0'}
    response = get_response(url)
    if response is None:
        return []
    if response.status_code == 200:
        json_response = json.loads(response.content.decode('utf-8'))
        return json_response['data']
    print(f"Found no page on the wiki using url: {url}. Possibly the subreddit does not exist.")


def get_wiki_page_content():
    wiki_page_content = {}
    base_url = 'https://www.reddit.com/r/genp/wiki/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    # ignored_pages = ['config/sidebar', 'config/description', 'config/stylesheet', 'config/submit_text', 'config/welcome_message' ]
    ignored_pages = []
    for page_name in get_wiki_pages_names():
        if page_name not in ignored_pages:
            url = base_url + page_name + '.json'
            print("Getting Data for: " + page_name, "URL: " + url)
            response = get_response(url)
            if response.status_code == 200:
                json_response = json.loads(response.content)
                wiki_page_content[page_name] = json_response['data']['content_md']
    return wiki_page_content


def save_wiki():
    wiki_page_content = get_wiki_page_content()
    base_location = ''
    if not wiki_page_content:
        return 
    for page_name in wiki_page_content:
        page_location = base_location + page_name + '.md'
        create_file(wiki_page_content[page_name], page_location)


def save_posts():
    base_location = 'posts/'
    post_urls = [
        "https://www.reddit.com/r/GenP/comments/yao439/update_compatibility_list_2023_creative_suite/",
        "https://www.reddit.com/r/GenP/comments/qpcnob/friendly_reminder_to_new_folks/",
        "https://www.reddit.com/r/GenP/comments/ue47y6/possible_solution_to_unlicensed_app_popup_no/"

    ]
    json_urls = []
    for url in post_urls:
        json_urls.append(url + '.json')
    headers = {'User-Agent': 'Mozilla/5.0'}
    for url in json_urls:
        response = get_response(url)
        if response is None:
            continue
        if response.status_code == 200:
            json_response = json.loads(response.content)
            post_title = json_response[0]['data']['children'][0]['data']['title']
            post_content = json_response[0]['data']['children'][0]['data']['selftext']
            post_location = base_location + post_title + '.md'
            create_file(post_content, post_location)
        else:
            print(f"Got Error {response.status_code} while downloading {url}.")

print("Starting Program")
save_wiki()
save_posts()
