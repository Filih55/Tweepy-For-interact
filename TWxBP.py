import tweepy

#api key : q7FEbx6RFLtsi4QnjC0hjGKtn
#api secret key : 6OVTsguY1UigGgv6P84YJZushNVFfUmlFkQD9TCDm6TzY4RkdT 
#accsess token  : 2726181840-oCgmuhDlPvCbkyOCdjB15XcYk0fNKr6VcmXGXEf
#accsess token secret : BcI7GKSYb1BU7UUChemQpMKPHOJGbKt9LEBgu5SHFn7zZ

auth = tweepy.OAuthHandler ("q7FEbx6RFLtsi4QnjC0hjGKtn","6OVTsguY1UigGgv6P84YJZushNVFfUmlFkQD9TCDm6TzY4RkdT")
auth.set_access_token("2726181840-oCgmuhDlPvCbkyOCdjB15XcYk0fNKr6VcmXGXEf","BcI7GKSYb1BU7UUChemQpMKPHOJGbKt9LEBgu5SHFn7zZ")
api = tweepy.API(auth, wait_on_rate_limit = True)

 # py TWxBP.py

og_tweet = api.get_status("	1347709702776320002		")


#img_obj = api.media_upload("1.jpg","2.jpg","3.jpg","4.jpg")
#new_status = api.update_status(" hello world")

#og_tweet = api.get_status("	1340256849489088512		")
#img_obj = api.media_upload("cute.jpg")
#my_reply = api.update_status(f"@{og_tweet.user.screen_name} Ahhhhh", og_tweet.id,media_ids=[img_obj.media_id_string])


my_reply = api.update_status(f"@{og_tweet.user.screen_name}  wkwkwkw mampos   ", og_tweet.id)