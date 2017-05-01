'''
Created on Mar 11, 2017

@author: Vicky
This file is to demonstrate the word frequency counter. This is a very important practical
'''
#!usr/bin/python3.5.2
from collections import Counter

text =  "Hello friend, hello friend. Maybe I should give you a name." \
        "The name is Elliot. I'm talking about the top 10 percent, the top 10 percent who trying to play God without our permission!!!" \
        "It was about last night. I should have been at Angela's birthday party. But instead, I went somewhere else"
        
words = text.split()
#print(words)

counter = Counter(words)
top_three = counter.most_common(5)
print(top_three)
##########################THE END OF PRACTICAL. BELOW IS EXPERIMENTAL SECTION #############################
key1 = counter.keys()
print(key1) #This is used to print all the keys in the list
value1 = counter.values()
print(value1) #This is used to print all the values of the keys in the list
item1 = counter.items()
print(item1) #This is used to print all the items along with its occurrence in the list
find_should = counter.__contains__('should')
#print_key = counter.__contains__keys()
#print(print_key)
print(find_should) #This is used to find whether the key you're searching for exists or not. O/P will be in True/False
item2 = counter.__getitem__("I")
print(item2) #This is used to find out how many times a particular key has occurred. O/P is in numeric.
'''
from collections import Hashable
hash1 = hash(words)
item3=hash1.__hash__()
print(item3)
'''
        