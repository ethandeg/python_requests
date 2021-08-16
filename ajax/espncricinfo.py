import requests
# THIS CODE HERE WILL GRAB 25 PAGES WORTH OF DATA AND SAVE TO TXT FILE FROM WEBSITE
with open('News.txt', 'w') as f:
    for i in range(1, 26):
        url = f'https://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page={i}'
        res = requests.get(url)

        data = res.json()

        for item in data:
            f.write(f"{item['author']} | {item['summary']}")
            f.write('\n')


# GRAB SUPER STATS FROM ESPN CRICKET WEBSITE
with open('Headlines.csv', 'w') as f:
    for i in range(1, 6):
        url = f"https://www.espncricinfo.com/ci/content/story/data/index.json?genre=706;;page={i}"
        res = requests.get(url)
        data = res.json()
        for headline in data:
            headline = headline['headline']
            headline = headline.replace(',', '|')
            f.write(headline)
            f.write('\n')
