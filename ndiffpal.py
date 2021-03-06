#@author:jubinchheda
#https://www.codechef.com/problems/NDIFFPAL
# First attempt

import sys
from sys import stdin
import fileinput
import math

from math import sqrt

def largestTr(n):
   return int(math.floor((1+sqrt(8*n+1))/2)-1)

def generateTriangles(largestNum, triangles):
   it = 1
   tr = 1
   while(tr<=largestNum):
      tr = triangular(it)
      triangles[it] = tr
   return	
 
def inputToList(stringList):
   for line in fileinput.input():
      stringList.append(line.rstrip())
   return stringList
   
def triangular(n):
   return (n*n+n)/2
   

def triangleList(n, resultSet):
   
   while(n>0):
      idx = largestTr(n)
      #print idx
      tr = triangular(idx)
      #print tr
      n=n-tr
      resultSet.append(idx)
   #print resultSet
   return
 
	  
      
def printPalindromeString(resultSet):
   chr = 97
   printStr = ""
   for item in resultSet:
      for i in xrange(int(item)):
	     #print chr
	     printStr = printStr + str(unichr(chr))
      chr = chr + 1
   print printStr
   
   
paramList = []
stringList = []
inputToList(stringList)


#N = int( stringList[0])
stringList.pop(0)

for item in stringList:
   paramList.append(int(item))
  
#print paramList
#largestNum = max(paramList)
#triangles = {}
#generateTriangles(largestNum, triangles)
for item in paramList:
   resultSet = []
   triangleList(item, resultSet)
   printPalindromeString(resultSet)
   
