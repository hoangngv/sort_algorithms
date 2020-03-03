integer_array = [19, 10, 11, 68, 3, 75, 71, 98, 31, 29, 1, 28, 18]

# bubble sort
def bubble_sort(array):
    n = len(array)
    # traverse through all array elements
    for i in range(n):
        # last i elements are already in place
        for k in range (0, n-i-1):
            # traverse the array from 0 to n-i-1
            # swap if the element found is greater than the next element
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]
    print("[Bubble sort] Sorted array in ascending order: ", array)

# selection sort
def selection_sort(array):
    n = len(array)
    # traverse through all array elements 
    for i in range(n): 
        # find the minimum element in remaining unsorted array 
        min_idx = i 
        for j in range(i+1, n): 
            if array[min_idx] > array[j]: 
                min_idx = j   
        # swap the found minimum element with the first element         
        array[i], array[min_idx] = array[min_idx], array[i]
    print("[Selection sort] Sorted array in ascending order: ", array)

bubble_sort(integer_array)
selection_sort(integer_array)