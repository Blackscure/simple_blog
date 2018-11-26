from database import Database
from models.post import Post


Database.initialize()


post = Post.from_mongo('ab8e363a2f9140298571cb3f0ee02008')

print(post)