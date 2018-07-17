import twitter
import time

api = api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')


search_results = api.GetSearch(term = "crispr", count = 2)


def tweet():
    for result in search_results:
        if result.favorite_count > 100:
            api.PostUpdate(result.text)
        else:
            print("Already tweeted for today.")

number_of_tweets = 0

while True:
    print("Looking for interesting articles...")
    if number_of_tweets <= 2:
        tweet()
        print("Tweeted!")
        number_of_tweets += 1
    else:
        print("Wait!")
        time.sleep(60*60*6)
        tweet()


