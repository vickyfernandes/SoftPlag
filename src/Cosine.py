'''
Created on Mar 13, 2017
@author: Vicky Fernandes
This program computes the cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)
'''
#!usr/bin/python3.5.2
import math

def cosine_similarity(v1,v2):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

v1,v2 = [3, 45, 7, 2], [2, 54, 13, 15]
print(v1, v2, cosine_similarity(v1,v2))