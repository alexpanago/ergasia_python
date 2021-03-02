import random

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 1, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    for count in range(nterms):
        if count == (nterms - 1):
            print(n1)
            n_oros = n1
            i = 0
            p = 0
            for i in range(20):
                value = random.randint(1, 1000)
                if (value ** n1) % n1 == value % n1:
                    p = p + 1
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
if p == 20:
    print("o arithmos", n_oros, "einai prwtos")
