import json

value = """
    {
        "title":"Tron: Legacy",
        "composer":"Daft Punk",
        "release_year":2010,
        "budget":null,
        "won_oscar":false
    }"""

tron = json.loads(value)
print(tron)

    