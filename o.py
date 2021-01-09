import tweepy



auth = tweepy.OAuthHandler("kiIRRtfQ8dS7AH3j3UmQIqpEV","QOBiq3n5bbwgjqjNXPzFLx8X1ToTfEvdKhqzaUIPzfe1PwfBDw")
auth.set_access_token("2726181840-uxTdhsoDuZp1wSpXplM80XlEYgIHx1mGlRnxmT7","UEqeIpcOdxp58uvubjA8QVJAnCb0REQdSq0mDMqW7iXnZ")
api = tweepy.API(auth, wait_on_rate_limit = True)

#      py o.py

#       cd C:\Users\User\AppData\Local\Programs\Python\Python38-32\Scripts


og_tweet = api.get_status("	1347333466795380736		")


#img_obj = api.media_upload("1.jpg","2.jpg","3.jpg","4.jpg")
#new_status = api.update_status(" hello world")

#og_tweet = api.get_status("	1340256849489088512		")
#img_obj = api.media_upload("cute.jpg")
#my_reply = api.update_status(f"@{og_tweet.user.screen_name} Ahhhhh", og_tweet.id,media_ids=[img_obj.media_id_string])


my_reply = api.update_status(f"@{og_tweet.user.screen_name}  xixix   ", og_tweet.id)

