import praw
import time
from datetime import datetime
import math
import NotifyUser
import FileM
#import CommentHandler

print ("==Dumbass bot initializing==")

r				= praw.Reddit(user_agent = "Script for learning purposes by /u/dynamicstatic")
exit			= False

print ("\n==============================")

while exit = False:
	run_bot(subtoget) #create loop with several subs
	time.sleep(2)
	print ("\n\n==============================\ncomments in list")
	for item in cache_link:
		print(item)
	check_comment_age(cache_link, cache_age)
	for item in cache_link:
		print(item)
	NotifyUser.send_msg('TESTING SHIT', cache_link, cache_age)
	FileM.save_file("test.data", cache_link)
	FileM.save_file("test2.data", cache_age)
	time.sleep(5000)

	#subreddit and cache_link in a class (?)
	#function to remove comment from cache_link
	#make whole bot run in separate thread, command thread running on the side as well. Check command thread every now and then.