import pickle

ingredients = []
filename = "test"
outfile = open(filename,"wb")
pickle.dump(ingredients, outfile)
outfile.close()