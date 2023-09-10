#def firstRepeatingElement(arr, n):
    #for i in range(n):
        #for j in range(i + 1, n):
            #if arr[i] == arr[j]:
                #return i
    #return -1

#if __name__ == '__main__':
    #arr = [10, 5, 3, 4, 3, 5, 6, 4]
    #n = len(arr)
    #index = firstRepeatingElement(arr, n)
    #if index == -1:
    #   print("No repeating element found!")
    #else:
    #   print("First repeating element is", arr[index])

################################################################################

#def bubbleSort(arr):
#    n = len(arr)
#   swapped = False
#  for i in range(n - 1):
#     for j in range(0, n - i - 1):
#            if arr[j] > arr[j + 1]:
#                swapped = True
#                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#       if not swapped:
#            return

#arr = [64, 34, 25, 12, 22, 11, 90]
#bubbleSort(arr)
#print("Sorted array is:")
#for i in range(len(arr)):
#   print("% d" % arr[i], end=" ")

################################################################################

#def selectionSort(array, size):
#    for ind in range(size):
#        min_index = ind
#        for j in range(ind + 1, size):
#            if array[j] < array[min_index]:
#                min_index = j
#        (array[ind], array[min_index]) = (array[min_index], array[ind])

#arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
#size = len(arr)
#selectionSort(arr, size)
#print('The array after sorting in Ascending Order by selection sort is:')
#print(arr)


################################################################################

#def mergeArrays(arr1, arr2, n1, n2, arr3):
#    i = 0
#    j = 0
#    k = 0
#    while (i < n1):
#        arr3[k] = arr1[i]
#        k += 1
#        i += 1
#    while (j < n2):
#        arr3[k] = arr2[j]
#        k += 1
#        j += 1
#    arr3.sort()

#if __name__ == '__main__':
#    arr1 = [1, 3, 5, 7]
#    n1 = len(arr1)

#   arr2 = [2, 4, 6, 8]
#    n2 = len(arr2)

#   arr3 = [0 for i in range(n1 + n2)]
#    mergeArrays(arr1, arr2, n1, n2, arr3)

#   print("Array after merging")
#   for i in range(n1 + n2):
#        print(arr3[i], end=" ")


################################################################################

#def isPrime(n):
#    if (n == 1 or n == 0):
#        return False

#    for i in range(2, int(n ** (1 / 2)) + 1):
#        if (n % i == 0):
#            return False
#    return True

#N = 100;
#for i in range(1, N + 1):
#    if (isPrime(i)):
#        print(i, end=" ")