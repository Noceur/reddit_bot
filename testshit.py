import praw
import time

r = praw.Reddit(user_agent = "Simple bot for learning purposes by /u/dynamicstatic")

print ("\n\n\n\n\n\n\n==============================")

cache = [['d340aln', 'https://www.reddit.com/r/test/comments/4isyzj/test/d340aln', '1', '406429.76944444445'], ['d33kbo7', 'https://www.reddit.com/r/test/comments/4j3up9/test/d33kbo7', '1', '406418.7727777778'], ['d33k455', 'https://www.reddit.com/r/test/comments/4j3zk5/testing/d33k455', '1', '406418.6825']]








indexid 					= 0
indexlink 					= indexid+1
indexscore 					= indexid+2
indexage					= indexid+3

#cache.append(comment.id)
#cache.append(comment.permalink)
#cache.append(comment.score)
#cache.append(comment_age)

def check_comments(cache):
	for item in cache:
		s = r.get_submission(indexlink)
		your_comment = s.comments[0]
		print (your_comment.id)
		#if (((your_comment.created_utc/60)/60)+120) >= ((time.time()/60)/60)


while True:
	subtoget = "test"
	#run_bot(subtoget)
	check_comments(cache)
	time.sleep(0)
	print ("comment id, comment permalink, comment score, comment unix age")
	for item in cache:
		#print(item)
		print(item[indexlink])
	time.sleep(100)