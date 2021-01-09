import tweepy
auth = tweepy.OAuthHandler("yYlQTWAQyasyrh2eDXqVsc24o", "Rjrp6fH6wJP3FWesWIst8S2gGVQfoCX9H5rMQY8zoXgw840fsb")
auth.set_access_token("2726181840-3n61vonKDmPwjKEL3JLqeSdNoeG4kXjeGLott24","qFMl1rJGfHj4ufHoYIiP2rxnNg5ldPGZEtmJLmldY51YB")
api = tweepy.API(auth)
tweet = input("  ")
api.update_status(status =(tweet))
print ("Done!")