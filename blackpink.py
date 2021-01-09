import random
import tweepy

#sedikit catatan kalo buat python jangan di kasih tab atau jaraka dari dinding kiri

auth = tweepy.OAuthHandler("yYlQTWAQyasyrh2eDXqVsc24o","Rjrp6fH6wJP3FWesWIst8S2gGVQfoCX9H5rMQY8zoXgw840fsb")
auth.set_access_token("2726181840-3n61vonKDmPwjKEL3JLqeSdNoeG4kXjeGLott24","qFMl1rJGfHj4ufHoYIiP2rxnNg5ldPGZEtmJLmldY51YB")
api = tweepy.API(auth)

def memify(text):
    new = []
    b =  '..ok boomber'
    for i in range(len(text)-len(b)):
        c = text[i]    
        r = random.randint(0,1)
    if  r:
        new.append(c.uper())
    else:
        new.append(c.lower())
    return ''.join(new + [b])
    
api.updates_status('hey its me')
commando









#cara untuk melihat sebuah tweet
status_obj = api.get_status("1332329820127191040")
print (status_obj.text)

#cara membalas tweet tersimpel haha
og_tweet = api.get_status("1332329820127191040")
# print(og_tweet.user.screen_name, og_tweet.id)
my_reply = api.update_status(f"@{og_tweet.user.screen_name} Wow this cool!", og_tweet.id)

#MEMBALAS TWEET DENGAN GAMBAR
og_tweet = api.get_status("1332335893802205186")
# print(og_tweet.user.screen_name, og_tweet.id)
img_obj = api.media_upload("CTH.jpg")

my_reply = api.update_status(f"@{og_tweet.user.screen_name} hahaha bgsadd", og_tweet.id,media_ids=[img_obj.media_id_string])

#UPLOAD STATUS DENGAN GAMBAAR 
img_obj = api.media_upload("CTH.jpg")
new_status = api.update_status("Hello world from the 30 Days of Python what up?", media_ids=[img_obj.media_id_string])





        python sa.py

api.update_status('@ wkwkwkw ga jadi serem jadinya',first_tweet.id) #<------untuk bales tweet------> 


#<----ini untuk bales tweet>
tweet = api.user_timeline(screen_name="FiersaBesari")	 
first_tweet = tweet[11]
print(first_tweet.text)




cd C:\Users\User\AppData\Local\Programs\Python\Python38-32\Scripts





for status in tweepy.Cursor(api.home_timeline).items(200):
     process_status(status);





     #TWITTER UNTUK ORANG KAYA 

     berear token :AAAAAAAAAAAAAAAAAAAAACObGgEAAAAAChxwfiRE0EnGqS2%2B4RnNFrwQ%2F8A%3DjsPUZuDO35I6ANEaOQmcRiX63zc1l8ohqCpSvYYDxWcCmUpEPw

acses toke : 2726181840-uxTdhsoDuZp1wSpXplM80XlEYgIHx1mGlRnxmT7

acses token skret : UEqeIpcOdxp58uvubjA8QVJAnCb0REQdSq0mDMqW7iXnZ




tweet = api.user_timeline(screen_name="nama user")
first_tweet = tweet[1]
print(first_tweet.text)



print("Berikut ini adalah 10 twit terakhir dari akun @nama user:\n")
i=1
for tweet in posts[:5]:
    print(str(i) +') '+ tweet.full_text + '\n')
    i= i+1


    #dibawah ini beda tai
    df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])



    #DATA AKUN UNTUK TWITTER FOR ORANG KAYA 
    auth = tweepy.OAuthHandler("kiIRRtfQ8dS7AH3j3UmQIqpEV","QOBiq3n5bbwgjqjNXPzFLx8X1ToTfEvdKhqzaUIPzfe1PwfBDw")
	auth.set_access_token("2726181840-uxTdhsoDuZp1wSpXplM80XlEYgIHx1mGlRnxmT7","UEqeIpcOdxp58uvubjA8QVJAnCb0REQdSq0mDMqW7iXnZ")
	api = tweepy.API(auth)