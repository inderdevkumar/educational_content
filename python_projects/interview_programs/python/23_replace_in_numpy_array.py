print("======  Program-23  ========")

import numpy as np

#array1= np.array([0,1,2,3,4,5,6,7,8,9]) 
# OR
array1= np.arange(0,10,1)

array1[array1 %2 != 0] = -1
print(array1)



#  Program to replace in list, same question but for list

list1= [0,1,2,3,4,5,6,7,8,9]

list_modified= [item  if item%2 == 0 else -1 for item in list1]

print(list_modified)
