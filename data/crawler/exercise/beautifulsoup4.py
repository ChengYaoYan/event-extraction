from bs4 import BeautifulSoup


with open('dormouse.html') as file_object:
	soup = BeautifulSoup(file_object, 'html.parser')
	print(soup.title)
	print(soup.title.name)
	print(soup.title.string)
	print(soup.title.parent.name)
	print(soup.p)
	print(soup.p['class'])
	print(soup.a)
	print(soup.find_all('a'))
	print(soup.find(href='link3'))
	print(soup.get_text())

with open('dormouse.html') as file_object:
	soup = BeautifulSoup(file_object, 'html.parser')
	links = soup.find_all('a')

	for link in links:
		print(link.get('href'))

