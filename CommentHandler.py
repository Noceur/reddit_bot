class CommentScraper:
	def __init__(self, name):
		subtoget					= name										# What subreddit to scan. (Use list and append name instead?)
		words_to_match				= []										# What words to look for i.e. albion.
		words_to_match_2			= []										# Secondary words to look for i.e. sucks.
		words_to_exclude			= []										# If these are found in the comment then disregards the comment (doesn't add it to watchlist).
		cache_link					= []										# List of links to found comments matching criteria. 
		cache_age					= []										# List of age to found comments matching criteria, index matches cache_link.
		hoursofcomments				= 0											# How many hours of comments you want to access.
		commentremovalage			= 0											# Decides how old a comment cant be (in hours) before it is removed from cache_link and cache_age.
		howfarbacktofetch 			= time.time() - (hoursofcomments*60*60)		# Takes hoursofcomments and multiplies it with seconds and minutes then subrtacts it from current time to figure out how far back to fetch.

	def add_words(self, matchlist, word):
		if matchlist = "match":
			self.words_to_match.append(word)
		elif matchlist = "match_2":
			self.words_to_match_2.append(word)
		else
			print ('Incorrect "matchlist", possible choices are "match" or "match_2"')

	def commentremovalage(self, removalage):
		self.commentremoval	= removalage

	def hoursofcomments(self, hours):
		self.hoursofcomments = hours

	def save_config(self): # Save subtoget, words_to_match, words_to_match_2, words_to_exclude, hoursofcomments and commentremovalage

	def load_config(self): #


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
		ageinhour = ((ageinsec/60)/60)
		return ageinhour