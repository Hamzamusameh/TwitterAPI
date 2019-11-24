from TweepyHelper import TweepyHelper

def main():
    consumerKey = input('Enter a consumer key: ')
    while not consumerKey:
        consumerKey = input('Enter a consumer key: ')
    consumerSecret = input('Enter a consumer secret: ')
    while not consumerSecret:
        consumerSecret = input('Enter a consumer secret: ')
    accessToken = input('Enter a access token: ')
    while not accessToken:
        accessToken = input('Enter a access token: ')
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