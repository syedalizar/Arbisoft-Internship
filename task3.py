from operator impot itemgetter

d = {2:3, 1:89, 4:5, 3:0}
sd = dict(sorted(d.items(), key=itemgetter(0))) #simplest method to sort simple dictionaries
#more complex ,ethod used in task 1

print sd
