'''
This module is used for pre-processing of python files.
'''

import re
import keyword

class Pyscp():

    def pscp(self,f1):
        #remove special characters from string and convert to lower-case 
        char_string=re.sub('[^a-zA-Z._]', ' ', f1).lower()
        
        #remove single occurrences of characters 
        final_string=re.sub(r'(?:^| )\w(?:$| )', '', char_string).strip() 
        
        reservedWords={} #empty list to store the reserved keywords
        reservedWords=keyword.kwlist #reserved keywords assigned to reservedWords list
        
        for word in reservedWords:
            #checking if reserved keyword exists in string or not
            if word in final_string:
                #substitute reserved keywords with no spaces
                final_string=re.sub(r'\b' + word +r'\b', '', final_string)
            else:
                continue 