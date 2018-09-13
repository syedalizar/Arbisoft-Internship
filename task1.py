
from collections import Counter

with open("updates") as words:
    txtlist = words.read().split()

countdict = (Counter(txtlist))
#Counter method counts instances of list values
#and returns a dictionary with the number of instances assigned to each unique instance in the dictionary


gen = ((k,v) for (k,v) in countdict.iteritems()) #generator use
sorteddict = sorted(gen, key=lambda x:x[1], reverse = True)
#generating a list of tuples from countdict
#then sorting it based on keys from the (key, value) tuples

sortedlist = sorted(countdict, key=lambda k: countdict[1], reverse = True) 
#remove reverse = True from arguments if ascending sort is required

print("Sorted Dictionary: ")
print( sorteddict ) #words in order with there occurence frequency

print("Sorted List: ")
print( sortedlist ) #words in order
