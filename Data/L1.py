import requests
from bs4 import BeautifulSoup

def scrape_and_append(url, output_file):
    """
    Scrapes text from the given URL and appends it to the specified output file.

    Parameters:
    - url: The webpage to scrape.
    - output_file: The file path where the scraped text will be appended.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text_data = "\n".join(para.get_text() for para in paragraphs)

    try:
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(text_data + "\n\n")
        print(f"Data from {url} appended to {output_file}")
    except IOError as e:
        print(f"File operation failed for {url}: {e}")

if __name__ == '__main__':
    # List of URLs for children's books
    urls = [
        'https://www.gutenberg.org/cache/epub/11/pg11-images.html',
        'https://www.gutenberg.org/cache/epub/67098/pg67098-images.html',
        'https://www.gutenberg.org/cache/epub/74/pg74-images.html',
        'https://www.gutenberg.org/cache/epub/55/pg55-images.html',
        'https://www.gutenberg.org/cache/epub/16/pg16-images.html',
        'https://www.gutenberg.org/cache/epub/10607/pg10607-images.html',
        'https://www.gutenberg.org/cache/epub/1430/pg1430-images.html',
        'https://www.gutenberg.org/cache/epub/54/pg54-images.html',
        'https://www.gutenberg.org/cache/epub/43936/pg43936-images.html',
        'https://www.gutenberg.org/cache/epub/7439/pg7439-images.html',
        'https://www.gutenberg.org/cache/epub/14838/pg14838-images.html',
        'https://www.gutenberg.org/cache/epub/902/pg902-images.html',
        'https://www.gutenberg.org/cache/epub/27200/pg27200-images.html',
        'https://www.gutenberg.org/cache/epub/236/pg236-images.html',
        'https://www.gutenberg.org/cache/epub/120/pg120-images.html',
        'https://www.gutenberg.org/cache/epub/2726/pg2726-images.html',
        'https://www.gutenberg.org/cache/epub/13/pg13-images.html',
        'https://www.gutenberg.org/cache/epub/770/pg770-images.html',
        'https://www.gutenberg.org/cache/epub/2306/pg2306-images.html',
        'https://www.gutenberg.org/cache/epub/19002/pg19002-images.html',
        'https://www.gutenberg.org/cache/epub/225/pg225-images.html',
        'https://www.gutenberg.org/cache/epub/3499/pg3499-images.html',
        'https://www.gutenberg.org/cache/epub/2786/pg2786-images.html',
        'https://www.gutenberg.org/cache/epub/20606/pg20606-images.html',
        'https://www.gutenberg.org/cache/epub/23661/pg23661-images.html',
        'https://www.gutenberg.org/cache/epub/2787/pg2787-images.html',
        'https://www.gutenberg.org/cache/epub/5343/pg5343-images.html',
        'https://www.gutenberg.org/cache/epub/641/pg641-images.html',
        'https://www.gutenberg.org/cache/epub/540/pg540-images.html',
        'https://www.gutenberg.org/cache/epub/1937/pg1937-images.html',
        'https://www.gutenberg.org/cache/epub/19/pg19-images.html',
        'https://www.gutenberg.org/cache/epub/501/pg501-images.html',
        'https://www.gutenberg.org/cache/epub/708/pg708-images.html',
        'https://www.gutenberg.org/cache/epub/20916/pg20916-images.html',
        'https://www.gutenberg.org/cache/epub/22566/pg22566-images.html',
        'https://www.gutenberg.org/cache/epub/25564/pg25564-images.html',
        'https://www.gutenberg.org/cache/epub/2781/pg2781-images.html',
        'https://www.gutenberg.org/cache/epub/146/pg146-images.html',
        'https://www.gutenberg.org/cache/epub/12/pg12-images.html',
        'https://www.gutenberg.org/cache/epub/24022/pg24022-images.html',
        'https://www.gutenberg.org/cache/epub/514/pg514-images.html',
        'https://www.gutenberg.org/cache/epub/46/pg46-images.html'






        'https://www.gutenberg.org/cache/epub/11/pg11-images.html',
        'https://www.gutenberg.org/cache/epub/67098/pg67098-images.html',
        'https://www.gutenberg.org/cache/epub/74/pg74-images.html',
        'https://www.gutenberg.org/cache/epub/55/pg55-images.html',
        'https://www.gutenberg.org/cache/epub/16/pg16-images.html',
        'https://www.gutenberg.org/cache/epub/10607/pg10607-images.html',
        'https://www.gutenberg.org/cache/epub/1430/pg1430-images.html',
        'https://www.gutenberg.org/cache/epub/54/pg54-images.html',
        'https://www.gutenberg.org/cache/epub/43936/pg43936-images.html',
        'https://www.gutenberg.org/cache/epub/7439/pg7439-images.html',
        'https://www.gutenberg.org/cache/epub/14838/pg14838-images.html',
        'https://www.gutenberg.org/cache/epub/902/pg902-images.html',
        'https://www.gutenberg.org/cache/epub/27200/pg27200-images.html',
        'https://www.gutenberg.org/cache/epub/236/pg236-images.html',
        'https://www.gutenberg.org/cache/epub/120/pg120-images.html',
        'https://www.gutenberg.org/cache/epub/2726/pg2726-images.html',
        'https://www.gutenberg.org/cache/epub/13/pg13-images.html',
        'https://www.gutenberg.org/cache/epub/770/pg770-images.html',
        'https://www.gutenberg.org/cache/epub/2306/pg2306-images.html',
        'https://www.gutenberg.org/cache/epub/19002/pg19002-images.html',
        'https://www.gutenberg.org/cache/epub/225/pg225-images.html',
        'https://www.gutenberg.org/cache/epub/3499/pg3499-images.html',
        'https://www.gutenberg.org/cache/epub/2786/pg2786-images.html',
        'https://www.gutenberg.org/cache/epub/20606/pg20606-images.html',
        'https://www.gutenberg.org/cache/epub/23661/pg23661-images.html',
        'https://www.gutenberg.org/cache/epub/2787/pg2787-images.html',
        'https://www.gutenberg.org/cache/epub/5343/pg5343-images.html',
        'https://www.gutenberg.org/cache/epub/641/pg641-images.html',
        'https://www.gutenberg.org/cache/epub/540/pg540-images.html',
        'https://www.gutenberg.org/cache/epub/1937/pg1937-images.html',
        'https://www.gutenberg.org/cache/epub/19/pg19-images.html',
        'https://www.gutenberg.org/cache/epub/501/pg501-images.html',
        'https://www.gutenberg.org/cache/epub/708/pg708-images.html',
        'https://www.gutenberg.org/cache/epub/20916/pg20916-images.html',
        'https://www.gutenberg.org/cache/epub/22566/pg22566-images.html',
        'https://www.gutenberg.org/cache/epub/25564/pg25564-images.html',
        'https://www.gutenberg.org/cache/epub/2781/pg2781-images.html',
        'https://www.gutenberg.org/cache/epub/146/pg146-images.html',
        'https://www.gutenberg.org/cache/epub/12/pg12-images.html',
        'https://www.gutenberg.org/cache/epub/24022/pg24022-images.html',
        'https://www.gutenberg.org/cache/epub/514/pg514-images.html',
        'https://www.gutenberg.org/cache/epub/46/pg46-images.html'
        
    ]

    output_file = "L1.txt"

    for url in urls:
        scrape_and_append(url, output_file)
