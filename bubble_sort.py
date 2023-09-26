import random as rand
arr = []
m = 0

def bubble_sort(array):
    print('Original Array:', array)
    j=0
    while j<len(array):
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        j += 1      
    print('Sorted Array:', array, end='\n\n')

while m < rand.randint(3, 10):
    for k in range(0,rand.randint(10,45)):
        arr.append(rand.randint(1,999))   
    m += 1  
    
    bubble_sort(arr)
    arr.clear()
                