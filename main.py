import tweepy
import json
import csv
import dotenv

dotenv.load()

consumer_key = dotenv.get('CONSUMER_KEY')
consumer_secret = dotenv.get('CONSUMER_SECRET')
access_token = dotenv.get('ACCESS_TOKEN')
access_token_secret = dotenv.get('ACCESS_TOKEN_SECRET')


# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        if 'coordinates' in decoded and decoded['coordinates'] is not None and 'text' in decoded:
            body_text = decoded['text'].encode('ascii', 'ignore')
            tweet_id = decoded['id']
            coordinates = decoded['coordinates']

            print body_text
            print decoded['id']

            with open('output.csv', 'a') as fp:
                a = csv.writer(fp, delimiter=',')
                the_data = [body_text, tweet_id, coordinates]
                a.writerow(the_data)

            print ''
            return True


def on_error(self, status):
    print status


if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    terms = ['asthma', 'copd', 'respiratory']

    print "Showing all new tweets for %s" % terms

    stream = tweepy.Stream(auth, l)
    stream.filter(track=terms, languages=['en'])
