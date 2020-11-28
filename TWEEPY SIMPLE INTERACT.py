import tweepy



auth = tweepy.OAuthHandler("	THIS IS YOUR TOKEN 	","	AND CONSUMER KEY		")
auth.set_access_token("		KEY SECRET	","		AND THE SECRET				")
api = tweepy.API(auth, wait_on_rate_limit = True)


#THIS THE COMMAND THAT YOU CAN USE FOR REPLAY OR JUST UPLOAD INTO YOUR TIMELINE

#THIS CODE IS FOR UPDATE STATUS IN YOUR TIMELINE
new_status = api.update_status("Hello world from the 30 Days of Python @Fidly_JKT48 what up?")


#THIS CODE IS A FOR YOU TO REPLAY COMMENT OR REPLAY ANY MENTIONS
og_tweet = api.get_status("1332329820127191040") # <--THIS IS AN ID FROM THE TWEET
my_reply = api.update_status(f"@{og_tweet.user.screen_name} Wow this cool!", og_tweet.id)


#REPLY WITH A IMAGE 
og_tweet = api.get_status("1332335893802205186")
img_obj = api.media_upload("CTH.jpg")
my_reply = api.update_status(f"@{og_tweet.user.screen_name} hahaha bgsadd", og_tweet.id,media_ids=[img_obj.media_id_string])


#MAKE TWEET WITH IMAGE ON IT 
img_obj = api.media_upload("CTH.jpg")
new_status = api.update_status("Hello world from the 30 Days of Python what up?", media_ids=[img_obj.media_id_string])


#THANKYOU SORRY FOR MY BAD ENGLISH AND MY CODING IS SUCK, BUT I HOPE THIS MAYBE HELP YOU