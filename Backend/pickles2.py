import pickle

empty_list = []
outfile = open("Ingredients","wb")
pickle.dump(empty_list,outfile)
outfile.close()
outfile = open("wrapIngredients","wb")
pickle.dump(empty_list,outfile)
outfile.close()
outfile = open("burgerIngredients","wb")
pickle.dump(empty_list,outfile)
outfile.close()
outfile = open("sides","wb")
pickle.dump(empty_list,outfile)
outfile.close()
outfile = open("drinks","wb")
pickle.dump(empty_list,outfile)
outfile.close()
