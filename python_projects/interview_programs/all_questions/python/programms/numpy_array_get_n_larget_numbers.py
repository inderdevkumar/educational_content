import numpy as np

array1= np.array([12,43,2,100,54,5,68])   # EXpecting o/p as [100 68]

#arrange numpy arrays in ascending order

index_sorted_array= np.argsort(array1)  #THis will get the index of soorted value
sorted_array= array1[index_sorted_array]
user_input= int(input("Enter n highest number to be taken from array: "))

larget_n_numbers= sorted_array[-user_input:]  # [68 100]

sort_in_desc= larget_n_numbers[::-1]
print("Original numpy array is: ",array1)
print(" Sorted Numpy array in ascending order is: " ,sorted_array)
print(f" Larget {user_input} numbers are: { larget_n_numbers}")
print(f" Largest {user_input} numbers as required are: {sort_in_desc}")
