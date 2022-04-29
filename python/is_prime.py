from math import sqrt
# This code is inefficient for very large numbers


def is_prime(number):
    """This function takes a number as an argument and returns 
    true if the number is a prime number, and false otherwise

    Args:
        number (number): any whole number

    Returns:
        boolean: True/False
    """
    if number <= 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            #print(f'{number} is divisible by {num}')
            return False
    else:
        return True


def list_primes(number):
    for n in range(number):
        if is_prime(n):
            print(n, end=' ')


list_primes(50)
print()


# More Efficient Code, even for large numbers
def is_primee(num):
    if num < 2 or num % 2 == 0 and num != 2:
        return False
    else:
        if num == 2 or num == 3:
            return True
    for x in range(3, int(sqrt(num))+1, 2):
        if num % x == 0:
            return False
    else:
        return True
