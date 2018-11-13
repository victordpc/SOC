#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv
import random
import sys

#argv[1] : number of nodes
#argv[2] : probability of two nodes having an edge
#argv[3] : path name for the csv


nNodes = sys.argv[1]
p = sys.argv[2]
PATHNODE = '%sNodes.csv'%(argv[3])
PATHEDGE = '%sEdges.csv'%(argv[3])
SEPARATOR = ','
HEADER_NODES = 'Id' + '\n'
HEADER_EDGE =  'Id' + SEPARATOR +'Source'+ SEPARATOR + 'Target' + '\n'


#Calculating number of edges with nNodes nodes and p probability
edgeSource[]
edgeTarget[]

for i in nNodes
    j = i
    while j < nNodes
        if p >= random.uniform(0, 1)
            edgeSource.append(i)
            edgeTarget.append(j)
		j += 1

#Debug
print 'Calculating edges OK'
#Generation of the node file .csv
fNode = open(PATHNODE,'w')
fNode.write(HEADER_NODES + '\n')
n = 0
while n < nNodes
	fNode.write(n + '\n')
	n += 1
fNode.close()
#Debug
print 'Generation of the node file: %s OK' % (PATHNODE)
#Generation of the edges file .csv
fEdge = open(PATHEDGE,'w')
fEdge.write(HEADER_EDGE +'\n')
for n in edgeSource
	fEdge.write(n + SEPARATOR + edgeSource[n] + SEPARATOR + edgeTarget[n] + '\n')
fEdge.close()
#Debug
print 'Generation of the edge file: %s OK' % (PATHEDGE)






