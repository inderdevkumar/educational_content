# ==========  1 Sorting of numbers ======================

def sort_number():

    list1= [2, 6, 5, 1, 3, 1, 4]

    for i in range(len(list1)-1):

        for j in range(len(list1)-1):  # or len(list1)-i-1 is better

            if list1[j]> list1[j+1]:

                temp= list1[j]
                list1[j]= list1[j+1]
                list1[j+1]= temp
    return list1

# print(sort_number())  # [1, 1, 2, 3, 4, 5, 6]

# ============ 2 Find a number is prime or not and get its factors =====================

def prime_or_not():

    n= int(input("Enter any number: "))
    

    list_of_factors= []
    if n>1:
        for i in range(2,n+1):
            if (n%i == 0):
                
                list_of_factors.append(i)
        
        if len(list_of_factors)==1:
            print(f"{n} Number is prime and factor is: {list_of_factors}")

        else:
            print(f"{n} Number is not prime and factor is: {list_of_factors}")
    else:
        print(f"{n} Number is not prime")


# prime_or_not()


# ============== 3 Get first n prime numbers ======================== Incomplete

def get_n_prime_numbers():
    
    n= int(input("Enter the limit for n prime numbers: "))
    
    list_of_primes= []

    for i in range(1, n+1):
        count= 0

        for j in range(2,n+1):

            if (i % j == 0):
                count= count+ 1

        if count == 1:
            list_of_primes.append(i)
        

    print(list_of_primes)

get_n_prime_numbers()

            
# ============= 4 Reverse a number =====================

def reverse_number():

    n= int(input("Enter number to get reversed: "))
    
    num= 0
    original_n= n

    while (n != 0):

        rem= n % 10
        num= num*10 + rem
        n= n//10

    print(f"REversed numnber of {original_n} is: {num}")

#reverse_number()

# ====== 5 Check if goiven number is palindrome or not ========================

def check_palindrome():
    n= int(input("Enter any number: "))

    num= 0
    original_n= n
    while n!= 0:

        rem= n % 10
        num= num*10 + rem
        n= n//10

    if (original_n == num):
        print(f"{original_n} = {num}. Hence, palindrome")
    else:
        print(f"{original_n} != {num}. Hence, not palindrome")

# check_palindrome()

# ============ 6 Check given number is armstrong number or not    ======================

def check_armstrong():

    n= int(input("Enter any numnber: "))

    original_n= n

    num= 0

    while(n != 0):

        rem= n % 10
        num= num+ (rem**3)
        n= n//10

    if (original_n == num):
        print(f"{original_n}= {num}. Hence, armstrong")

    else:
        print(f"{original_n} != {num}. Hence, not armstrong")


# check_armstrong()

# ========= 7 Check if number if binary or not ================

def check_binary():

    n= input("Enter any numnber: ")
    list1= []
    for item in n:

        if item == "1" or item == "0":
            list1.append("binary")
        
        else:
            list1.append("not binary")

    if all(item == "binary" for item in list1):
        print(f"{n} is binary")

    else:
        print(f"{n} is not binary")

# check_binary()

# ======= 8 FInd factorial of given number =============

def factorial():

    n= int(input("Enter any number: "))

    fact= 1

    for i in range(2, n+1):
        fact= fact*i
    
    print(fact)

# factorial()


# 9 Find fibonaci series for first n numbers  (0,1,1, 2, 3, 5...........)

def fibonacci():

    n= int(input("Enter limit: "))

    series= [0, 1]

    for i in range(2, n):

        next= series[i-2]+ series[i-1]
        series.append(next)
    
    print(series)

# fibonacci()

# ========== 10 Nested lists =====================

def nested_list(list1):

    new_list= []
    for item in list1:
        if type(item) == list:
            new_list.extend(nested_list(item))

        else:
            new_list.append(item)

    return new_list

# print(nested_list(['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']))

# 11 Decorator-> add the functionality of given function(INital functiom should add two numbers, with decorators add subtract)

def my_decorator(func1):
    
    print("DEcorator")

    def inner_func(a, b):

        print("Inner", (a-b))
        return func1(a, b)

    return inner_func

@my_decorator
def main(a, b):
    print("Main: ", (a+b))

"""
# main(4, 1) 

o/p:
DEcorator
Inner 3
Main:  5
"""
# ======= 12 Iterator example ====================

def iterator_use():

    list1= [2, 5, 7, 1, 2, 0]

    my_iter= iter(list1)
    print(next(my_iter))
    print(next(my_iter))

# iterator_use()  # 2, 5


# ======== 13 Generator example ======================

def genrator_use(a, b):

    yield a+b
    yield a-b
    yield a*b
    yield a/b
    yield a**b
    yield a//b

# print(list(genrator_use(4, 3)))  # [7, 1, 12, 1.3333333333333333, 64, 1]
    

# ======== 14 Use map_filter_reduce as  example ================

def map_filter_reduce_use():
    print("Please check in OOP text file")

# ========== 15 Use zip_lambda as example ==============

def zip_lambda_use():

    list1= [1, 2, 3, 4]
    list2= ["a", "b", "c", "d"]
    
    both_list= []
    for item1, item2 in zip(list1, list2):
        
        both_list.append((item1, item2))

    print("Using zip: ", both_list)

    
    x= lambda a, b, c: a+b+c

    add= x(2, 4, 1)
    print("Using lambda: ", add)

# zip_lambda_use()  # Using zip:  [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]     Using lambda:  7


# ======= 16 INteract with db, connection, update, insert =======


# 17 Mutable_immutable data types

def mutable_immuatble():

    # list and dictionary are mutable

    # string, tuple, set are immutable
    
    print("print l for list, d for dictionary, s for string, t for tuple and set for set")
    choice= input("enter your choice: ")

    if choice == "l" or choice == "d":

        list1= [1, "c", 3, 0]
        print(list1)

        list1[1]= 5
        print(list1)
        dict1= {"a": 1, "c": 4}
        print(dict1)

        dict1["c"]= 3
        print(dict1)

    else:

        s= "asdfgh"
        print(s)
        s[1]= "b"
        print(s)

# mutable_immuatble()


# ========= 18 Ordered_unordered data types ==================

def ordered_unordered():
    
    # Set and dictionray are un-ordered
    # list, string, tuple are ordered

    s1= "134"
    s2= "431"

    if (s1==s2):
        print("String is un-ordered")
    else:
        print("string is ordered")

# ordered_unordered()

# ========= 19 Find HCF and LCM of two numbers ====================

def hcf_lcm():

    a= int(input("Enter first number: "))
    b= int(input("Enter 2nd number: "))

    if a> b:
        greater= a

    else:
        greater= b


    while True:

        if (greater % a == 0 and greater % b == 0):
            lcm= greater
            break
        greater= greater+1

    print("LCM is: ", lcm)

    hcf= (a*b//lcm)

    print("HCF is: ", hcf)

#hcf_lcm()

# Count the occurance of each word and than print top 3 

def count_occurance():

    s1= """To create a database in MySQL, use the CREATE DATABASE statement:
           To create a table in MySQL, use the CREATE TABLE statement.
           To fill a table in MySQL, use the INSERT INTO statement.
           To select from a table in MySQL, use the SELECT statement:"""
    
    list1= s1.split()
    dict1= {}

    for item in list1:

        if item in dict1.keys():
            dict1[item]= dict1[item]+ 1

        else:
            dict1[item]= 1

    list2= [(value, key) for key, value in dict1.items()]
    list2.sort(reverse= True)
    print(list2[:3])

#count_occurance()


