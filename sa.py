import tweepy


#API KEY 				: rVxmlIhKnHpVgECva8dFC6eIb
#API SECRET KEY			: 3COjAaHZYWVVvSVMj7kZwvg04elEbnA9IGxXEP0FlhLSir41WA

#ACCSESS 				: 2726181840-mUkEejpyVURQ3b1NnFRzPqaPTD3hmZ0obqkijPi
#ACCSESS TOKEN SECRET 	: nIk1gi5yTDO7qyD8EIwGOeFsxUJHul8WOt8k7isAGs7U3

#         python sa.py

auth = tweepy.OAuthHandler("rVxmlIhKnHpVgECva8dFC6eIb","3COjAaHZYWVVvSVMj7kZwvg04elEbnA9IGxXEP0FlhLSir41WA")
auth.set_access_token("2726181840-mUkEejpyVURQ3b1NnFRzPqaPTD3hmZ0obqkijPi","nIk1gi5yTDO7qyD8EIwGOeFsxUJHul8WOt8k7isAGs7U3")
api = tweepy.API(auth, wait_on_rate_limit = True)


		
	
og_tweet = api.get_status("1337446053134573569")
my_reply = api.update_status(f"@{og_tweet.user.screen_name} Belum nih kan aku mahluk malam", og_tweet.id)