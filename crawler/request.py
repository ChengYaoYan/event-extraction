import requests


def getHtmlText(url):
	try:
		r = requests.get(url, timeout=30)
		# if the status code is not 200, then raise HTTP ERROR
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return 'Something wrong happend!'

result = getHtmlText('http://www.baidu.com')
print(result)


