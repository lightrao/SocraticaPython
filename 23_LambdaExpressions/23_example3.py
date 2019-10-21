mylist = [1, 2, 3, 4, 5]
mylist.sort(key=lambda x: -x)
print(mylist)

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clark", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)