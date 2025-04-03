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
        print(f"Request failed: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text_data = "\n".join(para.get_text() for para in paragraphs)

    try:
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(text_data + "\n\n")
        print(f"Data from {url} appended to {output_file}")
    except IOError as e:
        print(f"File operation failed: {e}")

if __name__ == '__main__':
    # Dictionary mapping categories to their respective URLs
    urls_by_category = {
        'children_books': [
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
            'https://www.gutenberg.org/cache/epub/120/pg120-images.html'
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
            'https://www.gutenberg.org/cache/epub/1937/pg1937-images.html'
            'https://www.gutenberg.org/cache/epub/19/pg19-images.html',
            'https://www.gutenberg.org/cache/epub/501/pg501-images.html',
            'https://www.gutenberg.org/cache/epub/19/pg19-images.html',
            'https://www.gutenberg.org/cache/epub/708/pg708-images.html',
            'https://www.gutenberg.org/cache/epub/20916/pg20916-images.html',
            'https://www.gutenberg.org/cache/epub/22566/pg22566-images.html',
            'https://www.gutenberg.org/cache/epub/25564/pg25564-images.html',
            'https://www.gutenberg.org/cache/epub/2781/pg2781-images.html',
            'https://www.gutenberg.org/cache/epub/146/pg146-images.html',
            'https://www.gutenberg.org/cache/epub/12/pg12-images.html',
            'https://www.gutenberg.org/cache/epub/24022/pg24022-images.html',
            'https://www.gutenberg.org/cache/epub/514/pg514-images.html',
            'https://www.gutenberg.org/cache/epub/46/pg46-images.html',




        ],
        'novels': [
            'https://www.gutenberg.org/cache/epub/67979/pg67979-images.html',
            'https://www.gutenberg.org/cache/epub/37134/pg37134-images.html',
            'https://www.gutenberg.org/cache/epub/37423/pg37423-images.html',
            'https://www.gutenberg.org/cache/epub/16317/pg16317-images.html',
            'https://www.gutenberg.org/cache/epub/12228/pg12228-images.html',
            'https://www.gutenberg.org/cache/epub/47403/pg47403-images.html',
            'https://www.gutenberg.org/cache/epub/45814/pg45814-images.html',
            'https://www.gutenberg.org/cache/epub/33460/pg33460-images.html',
            'https://www.gutenberg.org/cache/epub/13482/pg13482-images.html',
            'https://www.gutenberg.org/cache/epub/20220/pg20220-images.html',
            'https://www.gutenberg.org/cache/epub/1661/pg1661-images.html',
            'https://www.gutenberg.org/cache/epub/2009/pg2009-images.html',
            'https://www.gutenberg.org/cache/epub/59/pg59-images.html',
            'https://www.gutenberg.org/cache/epub/28553/pg28553-images.html',
            # Add more URLs as needed
        ],
        'news_articles': [
            'https://www.gutenberg.org/cache/epub/5001/pg5001-images.html',
            'https://www.gutenberg.org/cache/epub/50572/pg50572-images.html',
            'https://www.gutenberg.org/cache/epub/57421/pg57421-images.html',
            'https://www.gutenberg.org/cache/epub/852/pg852-images.html',
            'https://edition.cnn.com/2025/04/01/politics/takeaways-wisconsin-florida-election/index.html'
            'https://edition.cnn.com/2025/04/02/middleeast/israel-expands-military-operations-gaza-intl-hnk/index.html',
            'https://edition.cnn.com/2025/04/01/china/china-taiwan-drills-live-fire-escalation-intl-hnk/index.html',
            'https://edition.cnn.com/2025/04/01/asia/burst-gas-pipe-fire-malaysia-intl-hnk/index.html',
            'https://edition.cnn.com/2025/03/31/europe/ukraine-minerals-deal-trump-zelensky-intl/index.html',
            'https://edition.cnn.com/2025/04/02/middleeast/us-b2-bombers-diego-garcia-intl-hnk-ml/index.html',
            'https://edition.cnn.com/2025/04/02/business/liberation-day-trump-tariffs/index.html',
            'https://edition.cnn.com/2025/04/02/tech/ai-future-of-humanity-2035-report/index.html',
            'https://edition.cnn.com/2025/03/25/tech/china-robots-market-competitiveness-intl-hnk/index.html',
            'https://indianexpress.com/article/political-pulse/waqf-amendment-bill-live-updates-parliament-lok-sabha-rajya-sabha-9919305/?ref=breaking_hp',
            'https://indianexpress.com/article/explained/explained-global/susan-crawford-wisconsin-supreme-court-race-9920170/?utm_source=Taboola_Recirculation&utm_medium=RC&utm_campaign=IE&tbref=hp',
            # Add more URLs as needed
        ],
        'research_papers': [
            'https://arxiv.org/html/2504.00063v1',
            'https://arxiv.org/html/2504.00408v1',
            'https://arxiv.org/html/2504.00356v1',
            'https://arxiv.org/html/2504.00907v1',
            'https://arxiv.org/html/2504.00831v1',
            'https://arxiv.org/html/2504.00762v1',
            'https://arxiv.org/html/2504.00615v1',
            'https://arxiv.org/html/2504.00424v1',
            'https://arxiv.org/html/2504.00299v1',
            'https://arxiv.org/html/2504.00280v1',
            'https://arxiv.org/html/2504.00226v1',
            'https://arxiv.org/html/2504.00125v1',
            'https://arxiv.org/html/2504.00018v1',
            'https://arxiv.org/html/2504.00012v1',
            'https://arxiv.org/html/2410.08025v3',
            'https://arxiv.org/html/2503.21400v2',
            'https://arxiv.org/html/2504.00346v1',
            # Add more URLs as needed
        ]
    }

    # Iterate over each category and its URLs
    for category, urls in urls_by_category.items():
        output_file = f"{category}.txt"
        for url in urls:
            scrape_and_append(url, output_file)
