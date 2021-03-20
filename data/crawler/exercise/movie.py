import requests
from bs4 import BeautifulSoup


def get_html(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status()
		r.encoding = 'gbk'
		return r.text
	except:
		return 'Something wrong happend!'


def get_content(url):
	soup = BeautifulSoup(get_html(url), 'lxml')

	movies = soup.find('ul', class_='picList clearfix').find_all('li')

	for movie in movies:
		img_url = 'https:' + movie.find('img')['src']
		name = movie.find('span', class_='sTit').a.string

		try:
			time = movie.find('span', class_='sIntro').string
		except:
			time = '暂无上映时间'

		actors = movie.find('p', class_='pActor').find_all('a')
		actor_name = ''
		for actor in actors:
			actor_name += actor.string + ' '
		intro = movie.find('p', class_='pTxt pIntroShow').text

		print(f'movie name: {name}\t{time}\t{actor_name}\t{intro}')

		with open(f'{name}.png', 'wb+') as file_object:
			file_object.write(requests.get(img_url).content)


def main():
	url = 'http://dianying.2345.com/top/'
	get_content(url)


if __name__ == '__main__':
	main()