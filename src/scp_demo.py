'''
Created on 07-Apr-2017
@summary: Source-Code Pre-processing - Statement of Proof
@author: Vicky Fernandes
@organization: Don Bosco Institute of Technology, Mumbai.
'''
import math
import re
import keyword
reservedWords={} #empty list to store the reserved keywords
reservedWords=keyword.kwlist #reserved keywords assigned to reservedWords list

with open('circle.py', 'r') as file_input:
    f1 = file_input.read().lower()  #read file and convert to lower case
    
char_string=re.sub('[^a-zA-Z]', ' ', f1) #remove special characters from string
final_string=re.sub(r'(?:^| )\w(?:$| )', ' ', char_string).strip() #remove single occurrences of characters

for word in reservedWords:
    if word in final_string: #checking if reserved keyword exists in string or not
        final_string=re.sub(r'\b' + word +r'\b', ' ', final_string) #substitute reserved keywords with white spaces
    else:
        continue  
    
print(final_string) #print the final string without reserved keywords, upper case & single occurrences of characters

with open('file_output.txt', 'w') as file_output:
    f1 = file_output.write(final_string) #print output to file