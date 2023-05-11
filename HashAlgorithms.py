import itertools
"""
Some simple hashing algorithms to demonstrate how they work.
Salt...
"""

def simpleHash(message):
    """As this "hash" is just adding there will be collisions and many passwords can add up to the same number"""
    total = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    #look up position in alphabet and add position to total
    for i in range(len(message)):
        position = alphabet.index(message[i])
        total += position
    print("The super secure hash is = ", total)

#better hash
"""
Every number can be expressed as a product of its prime numbers i.e 255 = 3x5x17.
--> every number has a unique set of prime factors!
"""
def improvedHash(message):
    """
    abc will be 0,1,2 in the alphabet array. This maps to 2,3,5 in primes. 2x3x5 = 30.
    Every word will have a unique hash! Unlike the last one... BUT abc == cba!
    Being able to factorise numbers by primes will bust this!
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
    #each represent a letter a=2, c=3...
    total = 1 #or product
    for letter in range(len(message)):
        position = alphabet.index(message[letter]) #get index of each letter
        print(position, end=' ')
        total *= primes[position]
    print("\nHashed password =  ", total)

"""Next hash """
def betterHash(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
    total = 1
    prev = 0

    for letter in range(len(message)):
        position = alphabet.index(message[letter]) #get index of each letter
        #print(position, end=' ')
        total *= primes[position] + prev
        prev = total % 3989
    #print("\nHashed password =  ", total)

#improvedHash("athena")
#betterHash("abc")

"""Itertools to go through products and run them through the hashing algorithm"""
print(list(itertools.product("abc", repeat=2))) #'abc'= potential values, repeat = how many thing we want to check

#check for combinations... could be used with a hash function?
for combo in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3):
    print("".join(combo))

#hash all those values...
#can this be put into a while loop? repeat auto incrementing?
for combo in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3):
    new_hash = betterHash("".join(combo))
    #find target hash
    if new_hash == 2319212153792943360:
        print("".join(combo))




"""Can the target hash be broken?"""
targetHash = 2319212153792943360
def primeFactors(number):
    primeFactors = []
    factor = 2  # lowest prime factor
    while factor <= number:
        # If the number is divisible by the current factor, add it to the list of prime factors
        if number % factor == 0:
            primeFactors.append(factor)
            # Divide the number by the current factor and update the factor to 2
            number //= factor  # numberToFind is updated
            factor = 2
        # If the number is not divisible by the current factor, try the next one
        else:
            factor += 1
    print(primeFactors)
#primeFactors(2319212153792943360)















