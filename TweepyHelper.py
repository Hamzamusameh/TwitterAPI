import tweepy as tp

class TweepyHelper:
    def __init__(self, consumerKey, consumerSecret, accessToken, accessTokenSecret, tweetBody):
        self.consumerKey = consumerKey
        self.consumerSecret = consumerSecret
        self.accessToken = accessToken
        self.accessTokenSecret = accessTokenSecret
        self.tweetBody = tweetBody

    def PostTweet(self):
        try:
            auth = tp.OAuthHandler(self.consumerKey, self.consumerSecret)
            auth.set_access_token(self.accessToken, self.accessTokenSecret)
            api = tp.API(auth)
            api.update_status(self.tweetBody)
            print('A tweet is posted')
            return True
        except Exception as e:
            print(e, ' try again..')
            return False