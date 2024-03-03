import csv
import requests
from bs4 import BeautifulSoup

def get_movie_dialogue(url):
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            dialogue_section = soup.find('pre')
            dialogue_data = dialogue_section.text.strip()[:400].lower()
            dialogue_data = ' '.join(dialogue_data.split())

            return dialogue_data
        else:
            print(f'Failed to retrieve the page: {url}. Status code: {response.status_code}')
            return None
    except Exception as e:
        print(f'Error occurred while processing {url}: {e}')
        return None

def main():
    csv_file = 'cleaned_pudding_data.csv'
    
    dialogue_data_list = []
    
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            url = row[5]
            dialogue_data = get_movie_dialogue(url)
            if dialogue_data:
                dialogue_data_list.append({'URL': url, 'Dialogue': dialogue_data})
    
    output_file = 'pudding_movie_dialogue.csv'
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['URL', 'Dialogue'])
        writer.writeheader()
        writer.writerows(dialogue_data_list)
    
    print(f'Dialogue data saved to {output_file}')

if __name__ == '__main__':
    main()


