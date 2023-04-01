from instagrapi import Client

username = input("username: ")
password = input("Password: ")
client = Client()
client.login(username, password)

hashtag = input("Hashtag: ")
amount = int(input("amount: "))
posts = client.hashtag_medias_recent(hashtag, amount)

for i in range(amount):
    print("Post " + str(i + i))
    client.media_like(posts[i].id)
    print("liked post")
    client.user_follow(posts[i].user.pk)
    print("followed" + posts[i].user.username)