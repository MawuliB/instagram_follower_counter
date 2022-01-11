import requests
from bs4 import BeautifulSoup

try:
    user = "xbone_mawuli"
    url = "https://www.instagram.com/" + user
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    followers = soup.find("meta", {"name": "description"})["content"]
    follower_count = followers.split("Followers")[0]
    print("Followers = ", follower_count)

except TypeError:
    print("User Does not exist")
