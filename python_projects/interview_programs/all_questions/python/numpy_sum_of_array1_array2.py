import numpy as np

array1= np.array([1,2,3])
array2= np.array([4,5,6])

numpy_sum= np.sum((array1, array2), axis=0) # If axis=1 than it will be= [6, 15]
method2_sum_array= array1 + array2

print("Sum of array is: ", numpy_sum)
print("Sum of array is: ", method2_sum_array)
