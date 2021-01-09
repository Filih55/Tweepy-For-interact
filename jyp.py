import tweepy

#api key : 6NKTxzzS6OJbg3tcp08FLpnsf
#api secret key : o9BYGq6qYsERwV1fzREfTKMnNLnIwj4mvXe2XqoQC0Z3Nc7c5H

#accsess token  : 2726181840-tQPFFhl8CmjVaxzYwz7CAtuioD00yZcRMAA8Jv7
#accsess token secret : MwTk5mHScRYWsH0bdJhkpHxsvEvDbadlKUp0b7rBNhfgQ


#        python jyp.py

auth = tweepy.OAuthHandler("6NKTxzzS6OJbg3tcp08FLpnsf","o9BYGq6qYsERwV1fzREfTKMnNLnIwj4mvXe2XqoQC0Z3Nc7c5H")
auth.set_access_token("2726181840-tQPFFhl8CmjVaxzYwz7CAtuioD00yZcRMAA8Jv7","MwTk5mHScRYWsH0bdJhkpHxsvEvDbadlKUp0b7rBNhfgQ")
api = tweepy.API(auth, wait_on_rate_limit = True)


og_tweet = api.get_status("	1347328438038745088		")


#img_obj = api.media_upload("1.jpg","2.jpg","3.jpg","4.jpg")
#new_status = api.update_status(" hello world")

#og_tweet = api.get_status("	1340256849489088512		")
#img_obj = api.media_upload("cute.jpg")
#my_reply = api.update_status(f"@{og_tweet.user.screen_name} Ahhhhh", og_tweet.id,media_ids=[img_obj.media_id_string])


my_reply = api.update_status(f"@{og_tweet.user.screen_name}  hihi aku punya kontak jihyo loh  ", og_tweet.id)


