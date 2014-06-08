from slistener import SListener
import time, tweepy, sys

## authentication
# Consumer keys and access tokens, used for OAuth
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret='YOUR_CONSUEMR_SECRET'
access_token='YOUR_ACCESS_TOKEN'
access_token_secret='YOUR_SECRET_TOKEN'

 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def main():
    track = ["@MiamiHEAT", "@KingJames", "@ChrisBosh", "@Pacers", "@Paul_George24", "#NBAPlayoffs", "@NBA"]
    
    prefix = 'HeatPacers'

    listen = SListener(api, prefix)
    stream = tweepy.Stream(auth, listen)

    print "Streaming started..."

    try: 
        stream.filter(track = track)
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
