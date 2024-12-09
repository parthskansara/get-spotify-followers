import json
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options



import re 
from functools import reduce
from bs4 import BeautifulSoup

def parse_id (id_string):
    i = 24
    curr_id = []
    while id_string[i] != "-":
        curr_id += id_string[i]

    return "".join(curr_id)

def scrape_page(user_id, timeout=20):

    url = f"https://open.spotify.com/user/{user_id}/followers"

    options = Options()
    options.add_argument("--log-level=1")

    driver = webdriver.Chrome(options=options)
    follower_ids = set()

    try:
        # Set page load timeout
        driver.set_page_load_timeout(timeout)
        
        # Navigate to the URL
        driver.get(url)
        
        # Wait for the page to be fully loaded
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Additional wait to ensure dynamic content is loaded
        driver.execute_script("return document.readyState") == "complete"
        
        # Get the page source (HTML)
        html_content = driver.page_source

        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all 'p' tags with id starting with 'card-title-spotify:user'
        matches = soup.find_all('p', id=lambda x: x and x.startswith('card-title-spotify:user'))

        # Extract the 'title' attribute values
        titles = [tag['title'] for tag in matches]
        ids = [tag['id'] for tag in matches]

        json_array = [{"name": title, "id": id} for title, id in zip(titles, ids)]
        return json.dumps(json_array if json_array else [])
    
    except TimeoutException:
        print(f"Page load timed out after {timeout} seconds")

        return json.dumps({"error": "Timed out"})
    
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        try: 
            result = scrape_page(user_id)
            print(result)
        except Exception as e:
            print(e)
    else:
        print(json.dumps({"error": "No user ID provided"}))
