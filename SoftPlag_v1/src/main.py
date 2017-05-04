'''
Created on 25-Apr-2017

@author: Vicky Fernandes
@organization: Don Bosco Institute of Technology, Mumbai
'''

from SoftPlag import *
import os

inputdir = "/home/mindcraft/Desktop/vicky/python/SoftPlag_v1/src/input/"
outputdir = "/home/mindcraft/Desktop/vicky/python/SoftPlag_v1/src/output/"
filelist = os.listdir(inputdir)

if __name__ == '__main__':   
    for i in filelist:
        with open(os.path.join(inputdir + i), 'r') as f:
            fin = f.read()
            if i.endswith(".py"):               
                scp=Pyscp()    
                final_string = scp.pscpp(fin)
                scp.word_counter(final_string)
                with open(os.path.join(outputdir + i +".out"), 'w') as file_output:
                    file_output = open(os.path.join(outputdir + i +".out"), 'w')
                    file_output.write(final_string)
            
            if i.endswith(".java"):
                scp=Javascp()
                final_string=scp.jscpp(fin)
                scp.word_counter(final_string)
                with open(os.path.join(outputdir + i +".out"), 'w') as file_output:
                    file_output = open(os.path.join(outputdir + i +".out"), 'w')
                    file_output.write(fin)
