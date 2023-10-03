#!/usr/bin/python3

def fizzbuzz():
    """Play the Fizz Buzz game."""
    for num in range(1, 101):
        if (num % 15 == 0):
            print("FizzBuzz", end=" ")
        elif (num % 5 == 0):
            print("Buzz", end=" ")
        elif (num % 15 == 0):
            print("Fizz", end=" ")
        else:
            print(num, end=" ")
