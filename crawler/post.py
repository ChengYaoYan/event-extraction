'''
抓取百度贴吧---生活大爆炸吧的基本内容
爬虫线路： requests - bs4
Python版本： 3.7
'''
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

	li_tags = soup.findall('li', attrs={'class': ' j_thread_list clearfix thread_item_box'})
	print(li_tags[0])

get_content('https://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8&pn=100')
