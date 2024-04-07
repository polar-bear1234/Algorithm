# 快速排序
def quickSort(alist):
	quicksorthelper(alist, 0, len(alist)-1)
	return alist


def quicksorthelper(alist, first, last):
	if first < last:
		splitpoint = postion(alist, first, last)
		quicksorthelper(alist, first, splitpoint-1)
		quicksorthelper(alist, splitpoint+1, last)


def postion(alist, first, last):
	pivotvalue = alist[first]
	leftmark = first + 1
	rightmark = last
	done = True
	while done:
		while (leftmark <= rightmark) and (alist[leftmark] <= pivotvalue):
			leftmark += 1
		while (rightmark >= leftmark) and (alist[rightmark] >= pivotvalue):
			rightmark -= 1
		if rightmark < leftmark:
			done = False
		else:
			alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
	alist[first], alist[rightmark] = alist[rightmark], alist[first]
	return rightmark


if __name__ == "__main__":

	alist = [1,3,5,2,8,4,34,6,21,566,90,76,-23]
	print(alist)
	result = quickSort(alist)
	print(result)

	