'''
Created on 11-Apr-2017
@summary: Source-Code Pre-processing for Java files - Statement of Proof
@author: Vicky Fernandes
@organization: Don Bosco Institute of Technology, Mumbai.
'''
import re

with open('circle.java', 'r') as file_input:
    f1 = file_input.read().lower()  #read file and convert to lower case

def scp_java(f1):  
    char_string=re.sub('[^a-zA-Z]', ' ', f1) #remove special characters from string
    final_string=re.sub(r'(?:^| )\w(?:$| )', ' ', char_string).strip() #remove single occurrences of characters
    reservedWords={'abstract','continue','for','new','switch','assert',
                   'default','goto','package','synchronized','boolean','do',
                   'if','private','this','break','double','implements','protected',
                   'throw','byte','else','import','public','throws','case','enum',
                   'instanceof','return','transient','catch','extends','int','short',
                   'try','char','final','interface','static','void','class','finally',
                   'long','strictfp','volatile','const','float',
                   'native','super','while'} #list to store the reserved keywords
    for word in reservedWords:
        if word in final_string: #checking if reserved keyword exists in string or not
            final_string=re.sub(r'\b' + word +r'\b', ' ', final_string) #substitute reserved keywords with white spaces
        else:
                continue  
    
    print(final_string) #print the final string without reserved keywords, upper case & single occurrences of characters

    with open('file_output.txt', 'w') as file_output:
        f1 = file_output.write(final_string) #print output to file
        
        
scp_java(f1)