class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user): #methods always need a self parameter
        user.followers += 1
        self.following += 1


user_1 = User("001", "Michael")
user_2 = User("002", "Jack")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)