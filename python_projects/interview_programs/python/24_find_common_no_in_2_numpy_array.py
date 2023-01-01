print("====== Program-24 ===============")

import numpy as  np

print("Using numpy array")
array1= np.array([0,1,2,3,2,3,4,4,5,6])
array2= np.array([7,2,10,2,7,4,9,4,9,8])

common_array= np.intersect1d(array1,array2)
print(common_array)

# Same question for list

print("Using list")
list1= [0,1,2,3,2,3,4,4,5,6] 
list2= [7,2,10,2,7,4,9,4,9,8]

common_list= [item for item in list1 if item in list2]
print("LIst method 1 using set ")
print(list(set(common_list)))

print("List method2 using dict.fromkeys")
common_list= list(dict.fromkeys(common_list))  #Converting list dictionary keys and back to list. Key of dictionray can never have duplicat
print(common_list)
