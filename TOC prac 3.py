#Write a program for generating derivation sequence / language for the given sequence of productions
# A utility function that prints
# a given arr[] of length size#
def printArray(arr, size):
	for i in range(size):
		print(arr[i], end = " ")
	print()
	return

# This function returns 0 if there are
# no more sequences to be printed, otherwise
# modifies arr[] so that arr[] contains
# next sequence to be printed #
def getSuccessor(arr, k, n):

	# start from the rightmost side and
	# find the first number less than n
	p = k - 1
	while (arr[p] == n and 0 <= p < k):
		p -= 1

	# If all numbers are n in the array
	# then there is no successor, return 0
	if (p < 0):
		return 0

	# Update arr[] so that it contains successor
	arr[p] = arr[p] + 1
	i = p + 1
	while(i < k):
		arr[i] = 1
		i += 1
	return 1

# The main function that prints all sequences
# from 1, 1, ..1 to n, n, ..n
def printSequences(n, k):
	arr = [0] * k

	# Initialize the current sequence as
	# the first sequence to be printed #
	for i in range(k):
		arr[i] = 1

	# The loop breaks when there are
	# no more successors to be printed
	while(1):

		# Print the current sequence
		printArray(arr, k)

		# Update arr[] so that it contains
		# next sequence to be printed. And if
		# there are no more sequences then
		# break the loop
		if(getSuccessor(arr, k, n) == 0):
			break
	return

# Driver code
n = 4
k = 2
printSequences(n, k)
