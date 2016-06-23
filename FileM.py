import pickle
import os

def save_file(filename, datatosave):
	outfile = open(os.path.join(os.path.dirname(__file__), 'data', filename), "wb")
	pickle.dump(datatosave, outfile)
	outfile.close()
	print (filename + " saved successfully.")

def load_file(filename):
	infile = open(os.path.join(os.path.dirname(__file__), 'data', filename), "rb")
	output = pickle.load(infile)
	print (filename + " loaded successfully.")
	return output