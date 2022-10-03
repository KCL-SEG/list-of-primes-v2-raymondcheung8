"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError("The number entered must be above zero, exclusive!")

    list.append(2)
    nextNumber = 3

    for i in range(number_of_primes - 1):
        isNextPrime = False
        while not isNextPrime:
            for prime in list:
                if nextNumber % prime == 0:
                    break
            else:
                list.append(nextNumber)
                isNextPrime = True

            nextNumber += 2

    return list
