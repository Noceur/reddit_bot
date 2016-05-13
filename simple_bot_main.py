import praw
import time
from datetime import datetime
import math

print ("==Dumbass bot initializing==")

r = praw.Reddit(user_agent = "Simple bot for learning purposes by /u/dynamicstatic")
#r.login("Useless_bot_5003", "botbotbot")

print ("\n\n\n\n\n\n\n==============================")

#=====================================
#			VARIABLES
#=====================================

words_to_match 				= ["test"]
words_to_exclude 			= ["soccer", "football"]
cache 						= []
daysofcommentstofetch 		= time.time() - (1*5*60*60) #5 hours (for testing)
#index numbers, decides what to delete or modify
indexid 					= 0
indexlink 					= indexid+1
indexscore 					= indexid+2
indexage					= indexid+3


#=====================================
#			FUNCTIONS
#=====================================

def run_bot(subtoget):
	print ("==Getting subreddits==")
	subreddit = r.get_subreddit(subtoget)
	print ("Using subreddit: " + subtoget)
	comments = subreddit.get_comments(limit=None)
	print ("=========")
	check_comments(comments)

def check_comments(comments):
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in words_to_match)
		if comment.created_utc < daysofcommentstofetch: #compares the age of the comment to how many days the variable states, if the comment age is higher then it exits the function.
			return
		else:
			if comment.id not in cache and isMatch and comment.score >= 1:
				#cache.append(comment.id)
				comment_age = (((comment.created_utc)/60)/60)

				#watchlist_add(comment.id, comment.created)
				print ("Comment ID: \t\t\t" + comment.id + "\nComment permalink: \t\t" + comment.permalink + "\nComment score: \t\t\t" + str(comment.score))
				print ("comment age (hours): \t" + str(math.ceil(((time.time()-comment.created_utc)/60)/60)))
				print ("=========")

				#switch this out for a list in a list cache.append(comment.id, comment.permalink, comment.score) then loop through it with for item in cache: item[x]
				#use cache extend?
				cache.append(comment.id)
				cache.append(comment.permalink)
				cache.append(comment.score)
				cache.append(comment_age) #comment unix time age (from 1970 to the time comment was written)








#make function check comments 5 days back and compare to the stored number in cache


#def watchlist_clean(comment_age, comment_id):
	#use how_many_days_since_creation, if comment age > 10 then delete comment from cache
	#if comment_age >= 120:
		#comment_index = whateverlist.index(comment_id)


#def load_cache_from_file()

#def save_cache_to_file()

#def watchlist_add():
	#adds comment to watchlist

#def watchlist_update():



#def how_many_days_since_creation(comment):




while True:
	subtoget = "test"
	run_bot(subtoget)
	time.sleep(2)
	print ("comment id, comment permalink, comment score, comment unix age")
	for item in cache:
		print(item)
	time.sleep(100)