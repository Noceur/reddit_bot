import praw
import time
import math

r = praw.Reddit(user_agent = "Simple bot for learning purposes by /u/dynamicstatic")

print ("\n\n\n\n\n\n\n==============================")

cache = ['https://www.reddit.com/r/test/comments/4isyzj/test/d340aln', 'https://www.reddit.com/r/test/comments/4j3up9/test/d33kbo7', 'https://www.reddit.com/r/test/comments/4j3zk5/testing/d33k455',]




commentremovalage = 1 #in hours



indexid 					= 0
indexlink 					= indexid+1
indexscore 					= indexid+2
indexage					= indexid+3

#cache.append(comment.id)
#cache.append(comment.permalink)
#cache.append(comment.score)
#cache.append(comment_age)

def check_comments(cache):
	for item in sorted(cache, reverse=True):
		s = r.get_submission(item)
		your_comment = s.comments[0]
		if (((your_comment.created_utc)/60)/60+commentremovalage) <= ((time.time()/60)/60) : 
			print ("comment is older than " + str(commentremovalage) + " hours and will therefor get removed")
			cache.remove(your_comment.permalink)
		else :
			print ("comment not old enough to be deleted")
		print (((your_comment.created_utc)/60)/60+commentremovalage)
		print ((time.time()/60)/60)
		#if to_remove : 
			#for url in to_remove : 
				#cache.remove(url)
				#print (cache)

		#if str(item[indexage]+120) <= str(your_comment.created_utc/60/60) :
		#	print ("Removing comment" + your_comment.id)
		#else : 
		#	print ("Keeping comment")


		#print (your_comment.id)

		#if (((your_comment.created_utc/60)/60)+120) >= ((time.time()/60)/60):
		#	print ("delete comment")


while True:
	subtoget = "test"
	#run_bot(subtoget)
	check_comments(cache)
	time.sleep(0)
	print ("\n\n==============================\ncomments in list")
	for item in cache:
		print(item)
		#print(item[indexlink])
	time.sleep(100)