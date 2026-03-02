import requests
import bs4
import lxml

url = "https://habr.com/ru/feed/"
KEYWORDS = ['дизайн', 'фото', 'web', 'python',]

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, features='lxml')
articles_block = soup.select_one('div.tm-articles-list')
#print(articles_block)
articles_list = articles_block.select('article.tm-articles-list__item')
#print(len(articles_list))

parsed_data =[]
for i, article in enumerate(articles_list):
    
    if article['class'] == ['tm-articles-list__item', 'tm-articles-list__item_no-padding']:
       continue

    div_with_link = article.select_one('h2.tm-title_h2.tm-title')
    link ='https://habr.com' +  div_with_link.select_one('a')['href']

    response2 = requests.get(link)
    #print(link)
    span_title = div_with_link.select_one('span').text.strip()

    #print(Span_title)
    time_title = article.select_one('span.tm-user-info__user')
    time = time_title.select_one('time')['title']
    #print(time)
    count = 0
    for word in KEYWORDS:
        if span_title.find(word) != -1:
            count += 1
    for pp  in article.find_all('p'):
        #print(pp.text)
        for word in KEYWORDS:
            if pp.text.find(word) != -1:
                count += 1
    if count != 0:
        print(time)
        print(span_title)
        print(link)
        print('____________________')


