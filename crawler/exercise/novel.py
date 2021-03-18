import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'Something wrong happend!'


def get_book_information(url):
    '''
    collet category, name, address information of book
    return book's url list and write information into file
    '''
    soup = BeautifulSoup(get_html(url), 'lxml')
    urls = []

    categories = soup.find_all('div', attrs={'class': 'layout layout-col1'})

    for cate in categories:
        cate_name = cate.find('strong').string
        books = cate.find_all('ul')[3].find_all('span', class_='s2')

        with open('novel_list.csv', 'a+') as file_object:
            file_object.write(f'\nnovel category: {cate_name}\n')

        for book in books:
            link = 'http://www.qu.la' + book.a['href']
            title = book.a.string
            urls.append(link)
            with open('novel_list.csv', 'a') as file_object:
                file_object.write(f'novel-name: {title} \t novel-address: {link}\n')

    return urls


def get_chapters_url(book):
    '''
    get each chapter's url of a book
    '''
    soup = BeautifulSoup(get_html(book), 'lxml')
    urls = []

    book_name = soup.find_all('h2')[2].string[0:-2]
    chapters = soup.find_all('ul', class_='section-list fix')[1].find_all('li')
    chapters = chapters[1:]
    for url in chapters:
        urls.append('https://www.qu.la' + url.a['href'])

    return urls, book_name


def write_book(chapter, book_name):
    html = get_html(chapter).replace('<br/>', '\n')
    soup = BeautifulSoup(html, 'lxml')

    try:
        title = soup.find('h1', class_='title').string
        txt = soup.find('div', id='content').text.replace('chaptererror();', '')

        with open(f'/home/cyy/Workspace/event-extraction/crawler/exercise/book/{book_name}', 'a') as file_object:
            file_object.write(title + '\n\n')
            file_object.write(txt)
            print(f"novel {book_name}'s chapter {title} have been download finished!")
    except:
        print('Something wrong happend!')


def main(url):
    books = get_book_information(url)
    chapters, book_name = get_chapters_url(books[0])
    for chapter in chapters:
        write_book(chapter, book_name)


if __name__ == '__main__':
    url = 'https://www.qu.la/paihangbang/'
    main(url)
