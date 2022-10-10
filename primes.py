"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def primes(number_of_primes):
    number = 1
    list = []
    while len(list) < number_of_primes:
        for k in range(1,number+1):
            if number == 1 or (k != 1 and k != number and number % k == 0):
                break
            elif k == number:
                list.append(number)
        number+=1
    return list
