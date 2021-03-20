import bs4


soup = bs4.BeautifulSoup(open('dormouse.html'), 'lxml')
head_tag = soup.head
# print(head_tag)
# print(head_tag.contents)
title_tag = head_tag.contents[1]
# print(title_tag)
# print(title_tag.contents)
# for child in title_tag.children:
#  	print(child)

print(head_tag.descendants)
for child in head_tag.descendants:
	print(child)
