#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

#argv[1]: First probability for the subcritical net
#argv[2]: Second probability for the critical net
#argv[3]: Thrid probability for the supercritical net
#argv[4]: Fourth probability for the conected net

subcritical = sys.argv[1]
critical = sys.argv[2]
supercritical = sys.argv[3]
conected = sys.argv[4]

N1 = 500
N2 = 1000
N3 = 5000

SEPARATOR = ' '

PATH = 'python random_net.py'
pList = [subcritical,critical,supercritical,conected]
pathList = ['subcritical','critical','supercritical','conected']

j = 0
for i in pathList:
	os.system(PATH + SEPARATOR + str(N1) + SEPARATOR + str(pList[j]) + SEPARATOR + (pathList[j] + str(N1)))
	os.system(PATH + SEPARATOR + str(N2) + SEPARATOR + str(pList[j]) + SEPARATOR + (pathList[j] + str(N2)))
	os.system(PATH + SEPARATOR + str(N3) + SEPARATOR + str(pList[j]) + SEPARATOR + (pathList[j] + str(N3)))
	j += 1
