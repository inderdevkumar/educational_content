
"""
One of the coding questions was the following: Given a string S(input consisting) of '*' and '#'. The length of the string is variable. The task is to find the maximum number of '*' or '#' to make it a valid string. The string is considered valid if the number of '*' and '#' are equal. The '*' and '#' can be at any position in the string. 
"""

S= input("Enter any string only with */#: ")

print(len(S))

list_with_star= [item for item in S if item == "*"]

list_with_hash= [item for item in S if item == "#"]

print(list_with_star, len(list_with_star))
print(list_with_hash, len(list_with_hash))

if (len(list_with_star) == len(list_with_hash)):
    print("Its a valid string")

else:
    print("String is not valid")

    if (len(list_with_star) > len(list_with_hash)):
        print(f"We need {len(list_with_star) - len(list_with_hash)} # more to make it valid")
    else:
        print(f"We need {len(list_with_hash) - len(list_with_star)} * more to make it valid")
