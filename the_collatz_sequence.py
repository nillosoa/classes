#The Collatz conjecture(or sequence) is a conjecture in mathematics that concerns a sequence defined as follows:
#start with any positive integer n. Then each term is obtained from the previous term as follows:
#if the previous term is even, the next term is one half the previous term.
#If the previous term is odd, the next term is 3 times the previous term plus 1.
#The conjecture is that no matter what value of n, the sequence will always reach 1. -Wikipedia.


def collatz(number):
    #even number
    if (number % 2) == 0:
        print(number // 2)
        return number // 2

    #odd number
    elif (number % 2) == 1:
        print(3 * number + 1)
        return 3 * number + 1

number = int(input("Enter number: "))
while number != 1:
    number = collatz(number)
    