print("===================================================================")
print("Coding Exercise 1")

print("filenames = ['document', 'report', 'presentation']")

print("Copy-paste the above list in a .py file and extend the code, so it prints out the output below:")

print("0-Document.txt")
print("1-Report.txt")
print("2-Presentation.txt")


print("\n\n *****  Solution begins ************")
filenames= ['document', 'report', 'presentation']

for index, item in enumerate(filenames):
    print(f"{index}-{item.capitalize()}.txt")

print("\n\n ***** Coding1 ends here ************\n\n")
print("===================================================================")

#===================================================================

print("===================================================================")
print("Coding Exercise 2")
print("ips = ['100.122.133.105', '100.122.133.111']")

print("Copy-paste the ips list in a .py file and extend the program so it:")

print("1. Prompts the user to input an index (e.g, 0 or 1).")

print("2. Returns the IP address that has that index.")

print("Here is how the program would behave when executed:")
print("Eneter the INdex of the IP u want: 1")
print("You chose 100.122.133.111")

print("\n\n *****  Solution begins ************")

ips = ['100.122.133.105', '100.122.133.111']
user_input= int(input("Eneter the INdex of the IP u want: "))
print(f"You chose {ips[user_input]}")

print("\n\n ***** Coding2 ends here ************\n\n")
print("===================================================================")


