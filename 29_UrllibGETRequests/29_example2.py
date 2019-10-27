from urllib import request
from urllib import parse

# resp = request.urlopen("https://www.google.com/search?q=socratica")
params = {"v": "EuC-yVzHhmI", "t": "5m56s"}
querystring = parse.urlencode(params)
print(querystring)
url = "https://www.youtube.com" + "?" + querystring
resp = request.urlopen(url)
print(resp.isclosed())
print(resp.code)
html = resp.read().decode("utf-8")
print(html[:500])

