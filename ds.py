#!/usr/bin/env python

"""
2011 Facebook Hacker Cup Qualification Round Problem:
A double-square number is an integer X which can be expressed as the sum of two perfect squares.
Find all the double squares an int can be respresented in.
"""

import sys
import math
import logging


__author__ = "Sergio Bernales"
logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) < 1:
    sys.exit("Usage: ds <number>")
else:
    userNum = int(sys.argv[1])


uprSquareRoot = 0
midSquareRoot = 0


def determineSumsOfTwoSquares( num ):
    "Determine how many sums of squares the integer has"
    sumOfSquaresCount = 0
    usedSummandsSet = set()
    
    uprSquareRoot = int( math.sqrt(num) )
    midSquareRoot = int ( math.sqrt(num/2) )
    logging.debug('upper root: %d, mid root: %d\n', uprSquareRoot, midSquareRoot);
    
    #add bottom half ints to the dictionary
    print "Results:"
    for i in range(midSquareRoot, uprSquareRoot+1):
        diffSqrt = math.sqrt( num - (i*i))

        if (diffSqrt % 1 == 0 and (i*i) not in usedSummandsSet):
            #add summonds to set so as to not repeat them
            print "  ", i,"^ 2 + ", int(diffSqrt), "^ 2 = ", num
            usedSummandsSet.add(i*i);
            usedSummandsSet.add(diffSqrt*diffSqrt)

            sumOfSquaresCount+=1

    print "\nSum of squares count: ", sumOfSquaresCount, "\n"

     
if __name__ == "__main__":
    logging.debug("Started!")
    determineSumsOfTwoSquares(userNum)
