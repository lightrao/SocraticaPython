movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone with the Wind", "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz", "Gattaca", "Rear Window", "Ghostbusters", "To kill A Mockingbird", "Good Will Hunting", "2001: A Space Odyssey", "Raiders of the Lost Ark", "Groundhog Day", "Close Encounter of the Third Kind"]

gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)

gmovies2 = [title for title in movies if title.startswith("G")] 
print(gmovies2)
