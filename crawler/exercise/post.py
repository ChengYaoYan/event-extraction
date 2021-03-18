import requests
import time
from bs4 import BeautifulSoup


def get_html(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = 'utf-8'
		return r.text
	except:
		return 'Something wrong happend!'


def get_content(url):
	posts = []
	soup = BeautifulSoup(get_html(url), 'lxml')
	li_tags = soup.find_all('li', attrs={'class': 'j_thread_list clearfix thread_item_box'})

	for li in li_tags:
		post = dict()

		try: 
			post['title'] = li.find('a', attrs={'class': 'j_th_tit'}).text.strip()
			post['link'] = 'http://tieba.baidu.com/' + li.find('a', attrs={'class': 'j_th_tit'})['href']
			post['name'] = li.find('a', attrs={'class': 'frs-author-name'}).text
			post['time'] = li.find('span', attrs={'title': '创建时间'}).text
			post['replayNum'] = li.find('span', attrs={'title': '回复'}).text
			posts.append(post)
		except: print('Something wrong happend!')

	return posts


def write_to_file(posts):
	with open('TTBT.txt', 'a+') as file_object:
		for post in posts:
			file_object.write(f'title: {post["title"]} \t link: {post["link"]} \t name: {post["name"]} \t time: {post["time"]} \t replayNum: {post["replayNum"]}\n')

		print('Saved finish.')


def main(base_url, page_number):
	urls_list = []

	for pn in range(0, page_number):
		urls_list.append(base_url + str(50 * pn))
	print('All page have been downloaded already, readying to extract information.')

	for url in urls_list:
		content = get_content(url)
		write_to_file(content)
	print('Saved all information.')

base_url = 'https://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8&pn='
page_number = 3

if __name__ == '__main__':
	main(base_url, page_number)

