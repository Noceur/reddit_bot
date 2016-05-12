import praw
import time
from datetime import datetime
import math

print ("==Dumbass bot initializing==")

r = praw.Reddit(user_agent = "Simple bot for learning purposes by /u/dynamicstatic")
r.login("Useless_bot_5003", "botbotbot")

print ("\n\n\n\n\n\n\n ==============================")

words_to_match = ["test"]
words_to_exclude = ["soccer", "football"]
cache = []

def run_bot(subtoget):
	print ("==Getting subreddits==")
	subreddit = r.get_subreddit(subtoget)
	print ("Using subreddit: " + subtoget)
	comments = subreddit.get_comments(limit=100)
	print ("=========")
	check_comments(comments)
	#how_many_days_since_creation(comments)

def check_comments(comments):
	for comment in comments:
		comment_text = comment.body.lower()
		isMatch = any(string in comment_text for string in words_to_match)
		if comment.id not in cache and isMatch and comment.score >= 1:
			cache.append(comment.id)
			#watchlist_add(comment.id, comment.created)
			print ("Comment ID: \t\t" + comment.id + "\nComment permalink: \t" + comment.permalink + "\nComment score: \t\t" + str(comment.score))
			#commenttime = datetime.datetime.fromtimestamp(comment.created)
			#print (datetime.datetime.now() - commenttime)
			#print (comment.created)
			#print (how_many_days_since_creation(comment))
			print (math.ceil(((time.time()-comment.created_utc)/60)/60))
			print("=========")
			print ("is this in the branch?")

			#make function check comments 5 days back and compare to the stored number in cache
			'''
			import time
			import praw

			YESTERDAY = time.time() - (5*24*60*60)

			def get_todays(subreddit):
			    result = []
			    for post in subreddit.get_new(limit=None):
			        if post.created_utc < YESTERDAY:
			            return result
			        else:
			            result.append(post)

			r = praw.Reddit(user_agent='get_last_day_of_posts')
			sub = r.get_subreddit('learnpython')
			todays = get_todays(sub)
			'''

#def watchlist_clean():
	#use how_many_days_since_creation, if comment age > 10 then delete comment from cache

#def watchlist_add():
	#adds comment to watchlist

#def watchlist_update():


def how_many_days_since_creation(comment):


while True:
	subtoget = "test"
	run_bot(subtoget)
	time.sleep(2)