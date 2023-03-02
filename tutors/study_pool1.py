
def check_prime_and_get_factors():
    X= int(input("Enter your integer number: "))

    factor= []

    for num in range(1, X+1):
        if (X % num == 0):
            factor.append(num)
    
    if (len(factor) == 2):
        print(f"{X} is a prime numbers, as it has only two factors {factor}")

    else:
        print(f"{X} is not a prime numbers, as it has more than 2 factors {factor}")


def evaulate_equation():

    for X in range(-5, 5):
        Y= (8*X*X)+1
        print(Y)

check_prime_and_get_factors()
evaulate_equation()
