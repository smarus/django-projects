class Account:
    def __init__(self, media, username, n_followers):
        self.media = media
        self.username = username
        self.n_followers = n_followers
        print("Account")


# create the class here
class InstagramAccount(Account):
    def __init__(self, username, n_followers, n_following):
        self.media = 'Instagram'
        super().__init__(media=self.media, username=username, n_followers=n_followers)
        self.n_following = n_following
