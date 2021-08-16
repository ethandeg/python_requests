import requests

r = requests.get('https://quotes.toscrape.com')

html = r.text
with open('quotes.csv', 'w') as f:
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
            quote = line.strip()
        if ' <span>by <small class="author" itemprop="author">' in line:
            line = line.replace(' <span>by <small class="author" itemprop="author">', '').replace('</small>','')
            author = line.strip()
            f.write(f"{author}, {quote}")
            f.write('\n')