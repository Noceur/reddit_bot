import praw
import time
from datetime import datetime
import math
import NotifyUser
import FileM

print ("==Dumbass bot initializing==")

r = praw.Reddit(user_agent = "Learning purposes by /u/dynamicstatic")
#r.login("Useless_bot_5003", "botbotbot")

print ("\n\n\n\n\n\n\n==============================")

#=====================================
#			VARIABLES
#=====================================

subtoget					= "test"
words_to_match				= ["test"]
words_to_match_2			= ["sucks", "bad", "boring", "vaporware", "dumb", "shit", "trash", "censor", "censorship", "hate", "stupid", "nazi", "scam", "awful", "broken", "fail", "hate", "idiot"]
words_to_exclude			= ["soccer", "football"]
cache_link					= []
cache_age					= []
daysofcommentstofetch 		= time.time() - (1*3*60*60) #5 hours (for testing)
commentremovalage			= 1 #in hours
#index numbers, decides what to delete or modify
indexid						= 0
indexlink					= indexid+1
indexscore					= indexid+2
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
	#check_comments(comments)
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in words_to_match)
		print ("checked text in comment")
		if comment.created_utc < daysofcommentstofetch: #compares the age of the comment to how many days the variable states, if the comment age is higher then it exits the function.
			return
		else:
			if comment.permalink not in cache_link and isMatch and comment.score >= 1:
				print ("found one.")
				cache_link.append(comment.permalink)
				cache_age.append(timeunixtohour(comment.created_utc))
				

def check_comment_age(cache_link, cache_age):
	for index, item in sorted(enumerate(cache_link), reverse=True):
		if (cache_age[index]+commentremovalage) <= timeunixtohour(time.time()) : 
			print ("deleting index id: " + str(index))
			del cache_link[int(index)]
			del cache_age[int(index)]
		else :
			print ("comment not old enough to be deleted")


def timeunixtohour(ageinsec):
	ageinsec = ((ageinsec/60)/60)
	return ageinsec

	print ("test")
		


	



while True:
	run_bot(subtoget) #create loop with several subs
	time.sleep(2)
	print ("\n\n==============================\ncomments in list")
	for item in cache_link:
		print(item)
	check_comment_age(cache_link, cache_age)
	for item in cache_link:
		print(item)
	NotifyUser.send_msg('TESTING SHIT', cache_link, cache_age)
	time.sleep(5000)

	#subreddit and cache_link in a class (?)
	#function to remove comment from cache_link
	#make whole bot run in separate thread, command thread running on the side as well. Check command thread every now and then.