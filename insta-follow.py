from InstagramAPI import InstagramAPI
import getpass

username = input("enter username: ")
password = getpass.getpass(prompt = "enter password: ")

API = InstagramAPI(username, password)

if not API.login():
    print("Can't login!")
    exit()

user_id = API.username_id

# get followers and followings details
followers = API.getTotalFollowers(user_id)
followings = API.getTotalFollowings(user_id)

# get only followers and followings username
followers_username = [follower.get('username') for follower in followers]
followings_username = [following.get('username') for following in followings]

# find dayyoses :)
dayyooses = list(set(followings_username) - set(followers_username))

tmpCount = 1
for dayyoos in dayyooses:
    print("{}- {}".format(tmpCount, dayyoos))
    tmpCount += 1

# Show some numbers!
print('Number of followers:', len(followers_username))
print('Number of followings:', len(followings_username))
print('Number of dayyooses:', len(dayyooses))

# search in dayyooses list
search = input('Search for dayyoos? (y/n): ')
while search == 'y':
    name = input('Enter name: ')
    if name in dayyooses:
        print('%s is dayyoos' % name)
        search = input('Search for dayyoos? (y/n): ')
    else:
        print('%s is not dayyoos' % name)
        search = input('Search for dayyoos? (y/n): ')

print('follow me on github: http://github.com/amiremohamadi')
