#Project Euler 6

#Question
#<p>The sum of the squares of the first ten natural numbers is,</p>
#$$1^2 + 2^2 + ... + 10^2 = 385$$
#<p>The square of the sum of the first ten natural numbers is,</p>
#$$(1 + 2 + ... + 10)^2 = 55^2 = 3025$$
#<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
#<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>

def squared_sum(n):
	#squares n natural numbers then adds them
	final_sum=0
	for i in range (1,n+1):
		final_sum=final_sum + i**2
	return (final_sum)

def sum_squared(n):
	#Adds n natural numbers then squares them

	return (sum(range(1,n+1))**2)






#Test case
print(sum_squared(10))
print(squared_sum(10))
print(sum_squared(10)-squared_sum(10))

print("Final Total")

print(sum_squared(100)-squared_sum(100))

#Answer
#25164150