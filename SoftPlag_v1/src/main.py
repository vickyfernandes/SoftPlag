'''
Created on 25-Apr-2017

@author: Vicky Fernandes
@organization: Don Bosco Institute of Technology, Mumbai
'''

from SoftPlag import *
import os

if __name__ == '__main__':
    inputdir = "/home/mindcraft/Desktop/vicky/python/SoftPlag_v1/src/input/"
    outputdir = "/home/mindcraft/Desktop/vicky/python/SoftPlag_v1/src/output/"
    scpp=Pyscp()
    scpj=Javascp()
    filelist = os.listdir(inputdir)
    for i in filelist:
        if i.endswith(".py") or i.endswith(".java"):  # You could also add "and i.startswith('f')
            with open(inputdir + i, 'r') as f:
                fin = f.read()
                #if i.endswith(".py"):
                scpp.pscp(fin)
                #else:
                scpj.jscp(fin)
    
    
