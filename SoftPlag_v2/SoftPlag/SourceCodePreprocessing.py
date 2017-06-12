"""
#!usr/bin/Python3.6.1
Created on 25-Apr-2017

@author: Vicky Fernandes
@organization: Don Bosco Institute of Technology, Mumbai.
This module is used for pre-processing of python and Java files.
"""

import re
import keyword
import os
from collections import Counter

inputdir = "C:\input/"
outputdir = "C:\output/"

filelist = os.listdir(inputdir)

class Preprocessor:
    def scpp(self, fin):
        for i in filelist:
            # remove special characters from string and convert to lower-case
            char_string = re.sub('[^a-zA-Z._]', ' ', fin).lower()

            # remove single occurrences of characters
            final_string = re.sub(r'(?:^| )\w(?:$| )', '', char_string).strip()

            if i.endswith(".py"):
                reservedwords={}  # empty list to store the reserved keywords
                reservedwords = keyword.kwlist  # reserved keywords assigned to reservedWords list

            if i.endswith(".java"):
                reservedwords = {'abstract', 'continue', 'for', 'new', 'switch', 'assert',
                                 'default', 'goto', 'package', 'synchronized', 'boolean', 'do',
                                 'if', 'private', 'this', 'break', 'double', 'implements', 'protected',
                                 'throw', 'byte', 'else', 'import', 'public', 'throws', 'case', 'enum',
                                 'instanceof', 'return', 'transient', 'catch', 'extends', 'int', 'short',
                                 'try', 'char', 'final', 'interface', 'static', 'void', 'class', 'finally',
                                 'long', 'strictfp', 'volatile', 'const', 'float',
                                 'native', 'super', 'while'}  # list to store the reserved keywords

            for word in reservedwords:            # checking if reserved keyword exists in string or not
                if word in final_string:
                    # substitute reserved keywords with no spaces
                    final_string = re.sub(r' \b' + word + r'\b', '', final_string)

                else:
                    continue

        return final_string

    def word_counter(self, final_string):
        for i in filelist:

            words = final_string.split()
            counter = Counter(words)
            key = counter.keys()
            value = counter.values()
        print(key)
        print(value)

'''
#This is another logic for a word frequency counter. But I would mostly prefer using collections for simplicity purposes

            match_pattern = re.findall(r'\b' + r'[a-z]{2,1000}', final_string)
            frequency = {}
            for word in match_pattern:
                count = frequency.get(word, 0)
                frequency[word] = count + 1
                frequency_list = frequency.keys()
            
            #frequency_list = frequency.keys()
            print(frequency_list)
            for words in frequency_list:
                print(words, frequency[words])
'''