
from collections import Counter

with open("updates") as f:
    txtlist = f.read().split()

countdict = (Counter(txtlist))


gen = ((k,v) for (k,v) in countdict.iteritems()) #generator use
sorteddict = sorted(gen, key=lambda x:x[1], reverse = True)

sortedlist = sorted(countdict, key=lambda k: countdict[1], reverse = True) #remove reverse = True from arguments if ascending sort is required

print("Sorted Dictionary: ")
print( sorteddict ) #words in order with there occurence frequency

print("Sorted List: ")
print( sortedlist ) #words in order
