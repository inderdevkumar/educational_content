# write a program to print below # 10 # 9 8 # 7 6 5 # 4 3 2 1

#user_ip= int(input("Enter the highes_number: "))

# Mthod 1
n = 5
for i in range(n+1):
    for j in range(1, i+1):
        print(str(j), end='#')
