post2 = dict(message = "SS Cotopaxi", language = "English")
print(post2)
post2["user_id"] = 209
post2["datetime"] ="19771116T093001Z"
print(post2)
# print(post2['location'])

if 'location' in post2:
    print(post2['location'])
else:
    print('The post2 dose not contain a location value.')


try:
    print(post2['loaction'])
except KeyError:
    print("The post dose not have a loaction value.")


loc = post2.get('location', None)
print(loc)

