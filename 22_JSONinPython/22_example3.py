import json

movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton", "Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144ski"

# print(movie2)
file2 = open("22_JSONinPython\\movie_2.json", "w", encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False)
file2.close()
