'''
This module is used for pre-processing of java files in python.
'''
import re

class Javascp():

    def jscp(self,f1):  
        #remove special characters from string & convert to lower-case
        char_string=re.sub('[^a-zA-Z._]', ' ', f1).lower() 
        #remove single occurrences of characters
        final_string=re.sub(r'(?:^| )\w(?:$| )', '', char_string).strip()
        #list to store the reserved keywords
        reservedWords={'abstract','continue','for','new','switch','assert',
                   'default','goto','package','synchronized','boolean','do',
                   'if','private','this','break','double','implements','protected',
                   'throw','byte','else','import','public','throws','case','enum',
                   'instanceof','return','transient','catch','extends','int','short',
                   'try','char','final','interface','static','void','class','finally',
                   'long','strictfp','volatile','const','float',
                   'native','super','while'} 
        for word in reservedWords:
            #checking if reserved keyword exists in string or not
            if word in final_string: 
                #substitute reserved keywords with no spaces
                final_string=re.sub(r'\b' + word +r'\b', '', final_string) 
            else:
                continue