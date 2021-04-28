#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101, 1):
        if i%3 == i%5 == False:
            print("FizzBuzz", end=' ')
        elif i%3 == False:
            print("Fizz", end=' ')
        elif i%5 == False:
            print("Buzz", end=' ')
        else:
            print("{:d}".format(i), end=' ')
