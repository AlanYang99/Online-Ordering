#import pickle
import dill as pickle

empty_list = []
outfile = open("IngredientsD","wb")
pickle.dump(empty_list,outfile)
outfile.close()
outfile = open("Ingredients1D","wb")
pickle.dump(empty_list,outfile)
outfile.close()
outfile = open("wrapIngredientsD","wb")
pickle.dump(empty_list,outfile)
outfile.close()
outfile = open("burgerIngredientsD","wb")
pickle.dump(empty_list,outfile)
outfile.close()
outfile = open("sidesD","wb")
pickle.dump(empty_list,outfile)
outfile.close()
outfile = open("drinksD","wb")
pickle.dump(empty_list,outfile)
outfile.close()
