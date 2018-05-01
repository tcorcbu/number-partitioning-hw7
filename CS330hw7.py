# Homework 7 Problem 4
# Declan Halbert, Tom Cororan, Jim Mortenson 
import random
import numpy as np
#-------------------- Test 1 --------------------#
#This code was written for HW5

def kk(A):
  residue = 0
  max_nums = []
  while True:
      max_nums = getMaxNums(A)
      if 0 == max_nums[0] or 0 == max_nums[2]:
        residue = max(max_nums[0], max_nums[2])
        break
      residue = abs(max_nums[0] - max_nums[2])
      A[max_nums[1]] = residue
      A[max_nums[3]] = 0
  return residue

def getMaxNums(A):
  max1 = 0
  max1_idx = 0 
  max2 = 0 
  max2_idx = 0
  for i in range(len(A)):
    if A[i] > max1:
      max2 = max1
      max2_idx = max1_idx
      max1 = A[i]
      max1_idx = i
    elif A[i] > max2:
      max2 = A[i]
      max2_idx = i
  return [max1, max1_idx, max2, max2_idx]

#-------------------- End Test 1 --------------------#



#-------------------- Test 2 --------------------#
def randomsolutions(A):
	final = []
	while len(final) < 50:
		b = random.randint(-1, 1)
		if b == 0:
			continue
		final.append(b)

	c = abs(sum([a*b for a,b in zip(A,final)]))
	return c

#-------------------- End Test 2 --------------------#





#-------------------- Test 3 --------------------#


def testing(number):
	for i in range(50):
		final = []
		final2 = []
		testlist = random.sample(range(1,1000000000000), 50)
		if number == 1:
			for j in range(2500):
				final.append(kk(testlist))
			print("KK Algorithm -",i,min(final))
		if number == 2:
			for i in range(2500):
				final.append(randomsolutions(testlist))
			final2.append(min(final))
			print("Repeated Random -",i,min(final2))




testing(1)
testing(2)
