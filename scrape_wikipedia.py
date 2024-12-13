import requests
from bs4 import BeautifulSoup
import json
import os
def scrape_wikipedia(url, output_file):
    try:
       
        response = requests.get(url)
        response.raise_for_status()

        
        soup = BeautifulSoup(response.text, 'html.parser')

        
        title = soup.find('h1', {'id': 'firstHeading'}).text

        
        content = []
        for paragraph in soup.find_all('p'):
            text = paragraph.get_text(strip=True)
            if text:  
                content.append(text)

       
        data = {
            'title': title,
            'url': url,
            'content': content
        }

        
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Data successfully scraped and saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_json_in_vscode(file_path):
    try:
       
        os.system(f"code {file_path}")
        print(f"Opened {file_path} in VS Code.")
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")


if __name__ == "__main__":
    wikipedia_url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    output_filename = "web_scraping_data.json"
    scrape_wikipedia(wikipedia_url, output_filename)
    open_json_in_vscode(output_filename)

