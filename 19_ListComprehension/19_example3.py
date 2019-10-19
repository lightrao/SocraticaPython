movies = [("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life",1946), ("Gattaca", 1997), ("No Country for Old Men", 2007), ("Rear Window", 1954), ("The Lord of the Rings: The Fellowship of the Ring", 2001), ("Groundhg Day", 1993), ("Close Encounters fo the Third Kind", 1977), ("The Royal Tenenbaums", 2001), ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)]

pre2k = [title for (title, year) in movies if year < 2000]
print(pre2k)
