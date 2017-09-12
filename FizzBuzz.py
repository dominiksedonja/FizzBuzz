#!/usr/bin/env python
# -*- coding: utf-8 -*-

number = 0

while True:
    try:
        number = int(raw_input("Select a number between 1 and 100: "))
        for x in range(number):
            x += 1
            if (x % 3) == 0 and (x % 5) == 0:
                print "FizzBuzz"
            elif (x % 3) == 0:
                print "Fizz"
            elif (x % 5) == 0:
                print "Buzz"
            else:
                print x

    except ValueError:
        print('Invalid input.')
        continue