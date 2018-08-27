from InstagramAPI import InstagramAPI


username = input("enter username: ")
password = input("enter password: ")

API = InstagramAPI(username, password)
API.login()

user_id = API.username_id

# get followers and followings details
followers = API.getTotalFollowers(API.username_id)
followings = API.getTotalFollowings(API.username_id)

# get only followers and followings username
followers_username = [follower.get('username') for follower in followers]
followings_username = [following.get('username') for following in followings]

# find dayyoses :)
dayyooses = list(set(followings_username) - set(followers_username))

for dayyoos in dayyooses:
    print(dayyoos)
