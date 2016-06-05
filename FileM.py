import pickle

def save_file(tosave):
	outfile = open(tosave, "wb")
	pickle.dump(tosave, outfile)
	outfile.close()
	print (tosave + " saved successfully.")

def load_file(toload):
	infile = open(toload, "rb")
	output = pickle.load(infile)
	print (toload + " loaded successfully.")
	return output