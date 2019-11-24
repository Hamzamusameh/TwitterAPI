from TweepyHelper import TweepyHelper

def main():
    # '0HfMAVUeAQfUufv2pZzg7EzDE'
    consumerKey = input('Enter a consumer key: ')
    while not consumerKey:
        consumerKey = input('Enter a consumer key: ')
    # 'irvzHfdyatNobNlqUpU6f665B2sAncXzAOwcKqsVb64MqTYEdg'
    consumerSecret = input('Enter a consumer secret: ')
    while not consumerSecret:
        consumerSecret = input('Enter a consumer secret: ')
    # '1109485503437553664-rvobb7NiV8HdbMSHC2DTplOOyZMlPI'
    accessToken = input('Enter a access token: ')
    while not accessToken:
        accessToken = input('Enter a access token: ')
    # 'F1zNiChJzO3RQc0CcRc46C73yFjOUAw1BjI9s2Cw0wDEe'
    accessTokenSecret = input('Enter a access token secret: ')
    while not accessTokenSecret:
        accessTokenSecret = input('Enter a access token secret: ')
    tweetBody = input('Enter a tweet body: ')
    while not tweetBody:
        tweetBody = input('Enter a tweet body: ')

    t = TweepyHelper(consumerKey, consumerSecret, accessToken,
                accessTokenSecret, tweetBody)
    t.PostTweet()

main()