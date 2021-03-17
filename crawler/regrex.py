import re


re1 = r'[1-9]\d{5}'

num1 = '100'
num2 = '101000'
print(re.search(re1, num1))
print(re.search(re1, num2))

str1 = 'hello , world , life is short , use'
result1 = re.search(r'w.+d', str1, re.I)
print(result1)
# ?
result2 = re.findall(r'w.+d', str1, re.I)
print(result2)

str2 = 'hssso'
re1 = re.compile(r'h.{3}o')
print(re1.findall(str1))
print(re1.findall(str2))

d = re.search(r'e.+d', str1)
# print(d)
print(d.group())
print(d.string)
print(d.re)
print(d.pos)
print(d.endpos)
