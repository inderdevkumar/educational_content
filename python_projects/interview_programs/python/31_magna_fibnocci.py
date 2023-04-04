"""
 Write a program for Fibonacci series for n terms where n is the user input. 

0 1 1 2 3 5 ....
"""

n = int(input("Enter the range: "))

list1= [0, 1]
for i in range(1, n-1):
    list1.append(list1[i]+ list1[i-1])

print(list1, len(list1))



