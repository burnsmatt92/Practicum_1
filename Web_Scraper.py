import requests
import re
from bs4 import BeautifulSoup
import csv
import time

def extract_and_clean_text(url):

    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text(separator="\n\n", strip=True)

    text = " ".join(text.split())  
    text = re.sub(r'[^\w\s]', '', text)  

    return text

base_url = "https://www.d49.org"
visited_urls = set()
data = []
max_pages = 1000
max_crawl_time = 600  
start_time = time.time()

def crawl_website(url):
    print(url)

    # Time limit check
    elapsed_time = time.time() - start_time
    if elapsed_time > max_crawl_time:
        print("Maximum crawl time reached. Stopping crawl.")
        return

    if url in visited_urls:
        return 
    visited_urls.add(url)

    cleaned_text = extract_and_clean_text(url)
    if cleaned_text:
        data.append((url, cleaned_text))

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a', href=True):
            next_url = link['href']
            if next_url.startswith(base_url) and len(visited_urls) <= max_pages:
                crawl_website(next_url)
            elif next_url.startswith("/") and not next_url.startswith("//"):
                next_url = base_url + next_url
                crawl_website(next_url)

crawl_website(base_url)

# Write the data to CSV
with open("d49_scraped_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["URL", "Cleaned Text"]) 
    csvwriter.writerows(data)  

print("Data saved to d49_scraped_data.csv")
