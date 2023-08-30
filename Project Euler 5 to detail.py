#Project Euler 5

#Question
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Instead of working with the final digit, we can just look at the limiting input prime factors.

answer1 = (2**3)*(3**2)*5*7

answer = (2**4)*(3**2)*5*7*11*13*17*19

print(answer)

#This wasn't intended, but inspection is sometimes quicker than coding...

#Answer 
#232792560