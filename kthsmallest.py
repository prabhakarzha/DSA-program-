def kthSmallest(arr,n,k):

    arr.sort()

    return arr[k-1]

arr = [12, 3, 5, 7, 19]

n =len(arr)
k=2
print("k'th smallest element is",kthSmallest(arr,n,k))

#@
# A Python 3 program to put
# all negative numbers before
# positive numbers

def rearrange(arr, n ) :

	# Please refer partition() in
	# below post
	# https://www.geeksforgeeks.org / quick-sort / j = 0
	j = 0
	for i in range(0, n) :
		if (arr[i] < 0) :
			temp = arr[i]
			arr[i] = arr[j]
			arr[j]= temp
			j = j + 1
	print(arr)

# Driver code
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
n = len(arr)
rearrange(arr, n)


# This code is contributed by Nikita Tiwari.
