'''
Created on Apr 2, 2017

@author: Vicky Fernandes
below program takes input from 2 python files & calculates the frequency 
of the words encountered in the files
'''
#!usr/bin/python3.5.2
import math
import re

#count the frequency of words from file1
frequency1 = {}
file_input1 = open('circle.py', 'r')
f1 = file_input1.read().lower()
match_pattern1 = re.findall(r'\b[a-z]{3,15}\b', f1)
 
for word1 in match_pattern1:
    count1 = frequency1.get(word1,0)
    frequency1[word1] = count1 + 1
     
frequency_list1 = frequency1.keys()
 
for words1 in frequency_list1:
    print (words1, frequency1[words1])

print("----------END OF DISPLAY OF 1ST PYTHON FILE. 2ND PYTHON FILE DISPLAY BEGINS-------") 

#count the frequency of words from file2
frequency2 = {}
file_input2 = open('rect.py', 'r')
f2 = file_input2.read().lower()
match_pattern2 = re.findall(r'\b[a-z]{3,15}\b', f2)
 
for word2 in match_pattern2:
    count2 = frequency2.get(word2,0)
    frequency2[word2] = count2 + 1
     
frequency_list2 = frequency2.keys()
 
for words2 in frequency_list2:
    print (words2, frequency2[words2])
    
print("-------------END OF PROGRAM---------------------------------")    