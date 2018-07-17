import twitter
import time

api = api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')

search_results = api.GetSearch(term = "crispr", count = 2) #Find new CRISPR science articles.

def tweet():
    for result in search_results:
        if result.favorite_count > 100: #Get URLs with good traction (>100 favourites)
            api.PostUpdate(result.text)
        else:
            print("No good articles today. :(")

number_of_tweets = 0

while True:
    try:
        if number_of_tweets <= 2: #Only tweets 2 articles per day.
            tweet()
            number_of_tweets += 1
    except twitter.error.TwitterError as err:
        print(err)
        time.sleep(60*60*3) #Wait 3 hours before posting.
        tweet()
