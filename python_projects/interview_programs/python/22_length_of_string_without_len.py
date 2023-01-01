print("==========   Program 22 ============")

user_input= input("Enter your string: ")

print("Method -1, with len function ")
print("Length of string is: ", len(user_input))

print("Method-2, without len function")

count= 0
for item in user_input:
    count= count+1

print("Length of string is: ", count)

