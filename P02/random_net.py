#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv
import random
import sys

#argv[1] : number of nodes
#argv[2] : probability of two nodes having an edge
#argv[3] : path name for the csv


nNodes = int(sys.argv[1])
p = float(sys.argv[2])
PATHNODE = '%sNodes.csv'%(sys.argv[3])
PATHEDGE = '%sEdges.csv'%(sys.argv[3])
SEPARATOR = ','
HEADER_NODES = 'Id' + SEPARATOR + 'Label' + '\n'
HEADER_EDGE =  'Id' + SEPARATOR + 'Source' + SEPARATOR + 'Target' + '\n'

#Debug
print 'number of nodes:%d\n ' % (nNodes)

print 'probability: %f\n ' % (p)

print 'path of the node file:%s\n' % (PATHNODE)

print 'path of the edge file:%s\n' % (PATHEDGE)

#Generation of the node file .csv
fNode = open(PATHNODE,'w')
fNode.write(HEADER_NODES + '\n')
n = 0
while n < nNodes:
	fNode.write(str(n) + SEPARATOR + str(n) + '\n')
	n += 1
fNode.close()
#Debug
print 'Generation of the node file: %s OK' % (PATHNODE)

#Calculating number of edges with nNodes nodes and p probability and generation of edges file .csv
fEdge = open(PATHEDGE,'w')
fEdge.write(HEADER_EDGE +'\n')
pos = 0
for i in range(nNodes):
	j = i
	while j < nNodes:
		if(i != j):
			if p >= random.uniform(0, 1):
				fEdge.write(str(pos) + SEPARATOR + str(i) + SEPARATOR + str(j) + '\n')
				pos += 1
		j += 1

fEdge.close()
#Debug
print 'Generation of the edge file: %s OK' % (PATHEDGE)

