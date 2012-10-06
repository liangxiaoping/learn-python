# -*- coding: utf-8 -*-

# Insertion sort
# (1)insertSort(seq)
# (2)shellSort(seq)

# Exchange sort
# (1)bubbleSort(seq)
# (2)quickSort(seq, low, high)

# Selection sort
# (1)selectSort(seq)
# (2)heapSort(seq)

# Merge sort
# (1)mergeSort(seq)

def insertSort(seq):
	"""simple insertion sort"""
    # 0..i-1 sorted so far
	for i in range(1, len(seq)):
		for j in range(i, 0, -1):
			if seq[j-1] > seq[j]:
				seq[j-1], seq[j] = seq[j], seq[j-1]
	return seq

def bubbleSort(seq):
	"""Bubble sort"""
	n = len(seq)
	for i in range(0, n):
		for j in range(n-1, i, -1):
			if seq[j-1] > seq[j]:
				seq[j-1], seq[j] = seq[j], seq[j-1]
	return seq

# ugly
def quickSort(seq, low, high):
	"""Quick sort"""
	n = len(seq)
	if n <= 1:
		return seq

	if low < high:
		i, j, pivot = low, high, seq[low]

		while i < j:
			while i < j and seq[j] > pivot:
				j -= 1

			if i < j:
				seq[i], seq[j] = seq[j], seq[i]

			while i < j and seq[i] <= pivot:
				i += 1

			if i < j:
				seq[i], seq[j] = seq[j], seq[i]

		quickSort(seq, low, i-1)
		quickSort(seq, i+1, high)

	return seq

def quickSort2(seq):
	"""Quick sort using list comprehensions"""
	if seq == []:
		return []
	else:
		pivot = seq[0]
		lesser = quickSort2([x for x in seq[1:] if x < pivot])
		greater = quickSort2([x for x in seq[1:] if x >= pivot])
		return lesser + [pivot] + greater

def selectSort(seq):
	"""Selection sort"""
	n = len(seq)
	for i in range(0, n):
		minindex = i
		for j in range(i+1, n):
			if seq[j] < seq[minindex]:
				minindex = j
		if i != minindex:
			seq[i], seq[minindex] = seq[minindex], seq[i]
	return seq


print insertSort([49, 38, 65, 97, 76, 13, 27, 49])
print bubbleSort([49, 38, 65, 97, 76, 13, 27, 49])
print quickSort([49, 38, 65, 97, 76, 13, 27, 49], 0, 7)
print quickSort2([49, 38, 65, 97, 76, 13, 27, 49])
print selectSort([49, 38, 65, 97, 76, 13, 27, 49])