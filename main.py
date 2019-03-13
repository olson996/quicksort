from random import *

comparisons = 0

def quicksort1(A, left, right):
    if left >= right:
        return A
    (pivot_index, z) = partition(A, left, right)
    global comparisons
    comparisons += z
    quicksort1(A, left, pivot_index -1)
    quicksort1(A, pivot_index+1, right)


def quicksort2(A, left, right):
    if left >= right:
        return A

    middle = (left+right) // 2

    if A[middle] <= A[right] <= A[left]:
        A[right], A[left] = A[left], A[right]
    elif A[left] <= A[middle] <= A[right]:
        A[middle], A[left] = A[left], A[middle]
    elif A[right] <= A[middle] <= A[left]:
        A[left], A[middle] = A[middle], A[left]
    elif A[left] <= A[right] <= A[middle]:
        A[right], A[left] = A[left], A[right]
    
    (pivot_index, z) = partition(A, left, right)
    global comparisons
    comparisons += z
    quicksort2(A, left, pivot_index -1)
    quicksort2(A, pivot_index+1, right)

def quicksort3(A, left, right):
    if left >= right:
        return A
    x = randint(left, right)
    A[x], A[left] = A[left], A[x]
    (pivot_index, z) = partition(A, left, right)
    global comparisons
    comparisons += z
    quicksort3(A, left, pivot_index -1)
    quicksort3(A, pivot_index+1, right)



def partition(input_array, left_index, right_index):
    pivot = input_array[left_index]
    i = left_index + 1
    for j in range(left_index+1, len(input_array)):
        if input_array[j] < pivot:
            input_array[i], input_array[j] = input_array[j], input_array[i]
            i+=1
    input_array[left_index], input_array[i-1] = input_array[i-1], input_array[left_index]
    return i-1, right_index-left_index


def main():

    while True:
        try:
            print('Please enter a filename:')
            u_input = input()
            f = open(u_input, 'r')
            read_file = f.read().split('\n')[:-1]
            while True:
                try:
                    print('Please enter a Quicksort variant:')
                    u_input = input()
                    y = ['first', 'median3', 'random']
                    if u_input not in y:
                        raise NameError
                    arr = [int(num_str) for num_str in read_file]
                    arr = arr[1:]
                    if u_input == 'first':
                        quicksort1(arr, 0, len(arr)-1)
                    elif u_input == 'median3':
                        quicksort2(arr, 0, len(arr)-1)
                    else:
                        quicksort3(arr, 0, len(arr)-1)
                    break
                except NameError:
                    print('Incorrect variant. Options are "first", "median3", or "random".')
            break
        except OSError:
            print('File does not exist.\n')
    print(comparisons)
main()
