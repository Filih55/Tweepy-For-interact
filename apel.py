import tweepy

#api key : MEgcJDkf3Cc4hXpwVPFC0j2ym
#api secret key : Ok8L7clNWCo29RnezLemFCA3pK80xtymGjathnR1tKtafAkYwR 
#accsess token  : 2726181840-tk8apk24e9L4GOmGbkq1t7RQxRsueIL3AhC9GqU
#accsess token secret : yN26LG8oy4nq0ThaXeCjeKDfgPA18iXFaCkDIYXLR6uyv

auth = tweepy.OAuthHandler ("MEgcJDkf3Cc4hXpwVPFC0j2ym","Ok8L7clNWCo29RnezLemFCA3pK80xtymGjathnR1tKtafAkYwR")
auth.set_access_token("2726181840-tk8apk24e9L4GOmGbkq1t7RQxRsueIL3AhC9GqU","yN26LG8oy4nq0ThaXeCjeKDfgPA18iXFaCkDIYXLR6uyv")
api = tweepy.API(auth, wait_on_rate_limit = True)


#og_tweet = api.get_status("1347718980530626564")

img_obj = api.media_upload("pp.jpg")
new_status = api.update_status(" udah lama ga main mobile legend  ", media_ids=[img_obj.media_id_string])

#new_status = api.update_status(" udah lama ga buka mobile legend... ")

#img_obj = api.media_upload("1.jpg","2.jpg","3.jpg","4.jpg") 

#og_tweet = api.get_status("	1340256849489088512		")

#my_reply = api.update_status(f"@{og_tweet.user.screen_name} Ahhhhh", og_tweet.id,media_ids=[img_obj.media_id_string])


#my_reply = api.update_status(f"@{og_tweet.user.screen_name}  udah daritadi ip   ", og_tweet.id)