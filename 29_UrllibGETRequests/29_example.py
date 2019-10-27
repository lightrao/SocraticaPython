from urllib import request

resp = request.urlopen("https://www.baidu.com")
# print(type(resp))
# print(resp.code)
# print(resp.length)
# print(resp.peek())

data = resp.read()
print(type(data))
print(len(data))
html = data.decode("UTF-8")
print(type(html))
print(html)
