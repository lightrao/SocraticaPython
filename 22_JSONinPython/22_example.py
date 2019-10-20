import json

json_file = open("22_JSONinPython\\movie_1.txt", "r", encoding = "utf-8")
movie = json.load(json_file)
json_file.close()

print(movie)
print(type(movie))
print(movie["title"])
print(movie["actors"])
print(movie["release_year"])
print(json.dumps(movie, ensure_ascii=False))
