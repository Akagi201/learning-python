#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke


#bubbleSort algorithm
def bubbleSort(n):
    for j in xrange(len(n),-1,-1):
        for i in xrange(0,j-1,1):
            if n[i] > n[i+1]:
                n[i],n[i+1] = n[i+1],n[i]


#test
if __name__=='__main__':
	numbers=[[9,23,12,32,12],['2', '3', '3', '6'],['b','w','u']]
	for num_list in numbers:
	    bubbleSort(num_list)
	    print num_list
