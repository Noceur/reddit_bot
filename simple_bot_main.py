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

			#make function check comments 10 days back and compare to the stored number in cache
			'''
			import time
			import praw

			YESTERDAY = time.time() - (24*60*60)

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
	#for comment in comments:

		#Kill me now
		#comment_time = comment.created_utc
		#current_time = time.strftime('%s', time.gmtime())
		#current_time = datetime(2012,4,1,0,0).timestamp()
		#print (current_time)
		#print (comment_time)
		#calc_time = ((((current_time - comment_time)/60)/60)/24)
		#print (calc_time)
		
	#parsed_date_comment = datetime.utcfromtimestamp(comment.created_utc)
	#parsed_date_now = datetime.utcnow()
	#time_now = time.time()
	#time_comment = comment.created_utc
	#day_comment = parsed_date_day
	'''
	year_comment = parsed_date_comment.year
	month_comment = parsed_date_comment.month
	day_comment = parsed_date_comment.day
	hour_comment = parsed_date_comment.hour
	year_now = parsed_date_now.year
	month_now = parsed_date_now.month
	day_now = parsed_date_now.day
	hour_now = parsed_date_now.hour
	'''
	#howmanydays = ((year_comment*365*24)+(month_comment*30*24)+(day_comment*24)+hour_comment)-((year_now*365*24)+(month_now*30*24)+(day_now*24)+hour_comment)
	#print (currentday)
	#print (time_comment)
	#print (time_now)
	#print (math.ceil(((time.time()-comment.created_utc)/60)/60))
	#return howmanydays


while True:
	subtoget = "test"
	run_bot(subtoget)
	time.sleep(2)