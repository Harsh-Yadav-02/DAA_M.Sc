import random as random
import matplotlib.pyplot as plt


def insertion_sort(array):
    cmp = 0
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j>= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
            cmp += 1
        array[j+1] = key  
    cmp_list.append(cmp)    
    print(cmp) 

cmp_list = []
array = []
k=1
while k<11:
   for i in range(10):
    array.append(random.randint(1, 1000))
   print('Original',array,end="\n")
   print('No. of comparisons:', end='')
   insertion_sort(array)
   print('Sorted',array)
   
   print()
   array.clear()
   k += 1
print("Comparison List:", cmp_list)  
print("Best Case Comparisons:", min(cmp_list)) 
print("Average Case Comparisons:", (sum(cmp_list))/10) 
print("Worst Case Comparisons:", max(cmp_list)) 
plt.scatter(cmp_list,range(1,11))
plt.show()