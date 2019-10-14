# FriendFace post

post = {"user_id":209, "message":"D5 E5 C5 C4 G4", "language":"English", "datetime":"20230215T124231Z", "location":(44.590553, -104.715556)}
print(post)
light = {True:1, False:2, 3.14:"pi", 18:"age"}
print(light)
print(light[True])
print(light[3.14])

print(type(post))

print(post['message'])

for key in post.keys():
    value = post[key]
    print(key, "=", value)


print()


for key, value in post.items():
    print(key, '=', value)

print()

var = post.pop('user_id')
print(var)
print(post)
