'''
Created on 25-Apr-2017

@author: Vicky Fernandes
@organization: Don Bosco Institute of Technology, Mumbai
'''

from SoftPlag import *
import os

# inputdir = "/home/mindcraft/Desktop/vicky/python/SoftPlag_v1/src/input/"
inputdir = "C:\input/"
# outputdir = "/home/mindcraft/Desktop/vicky/python/SoftPlag_v1/src/output/"
outputdir = "C:\output/"
filelist = os.listdir(inputdir)

if __name__ == '__main__':
    for i in filelist:
        with open(os.path.join(inputdir + i), 'r') as f:
            fin = f.read()
            proc = Preprocessor()
            final_string = proc.scpp(fin)
            proc.word_counter(final_string)
            with open(os.path.join(outputdir + i + ".out"), 'w') as file_output:
                file_output = open(os.path.join(outputdir + i + ".out"), 'w')
                file_output.write(final_string)
