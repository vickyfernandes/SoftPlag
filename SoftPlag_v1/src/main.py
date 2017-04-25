'''
Created on 25-Apr-2017

@author: Vicky Fernandes
@organization: Don Bosco Institute of Technology, Mumbai
'''

from SoftPlag import *

if __name__ == '__main__':
    with open('circle.java', 'r') as file_input:
            f1 = file_input.read() 
    
    scpp=Pyscp()
    scpp.pscp(f1)
    
    scpj=Javascp()
    scpj.jscp(f1)
    
    def fileout(self,final_string):
        print(final_string)
        with open('file_output.txt', 'w') as file_output:
            f1 = file_output.write(final_string) #print output to file

    

    
    