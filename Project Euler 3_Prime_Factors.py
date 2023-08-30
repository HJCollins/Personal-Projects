#Project Euler 3

#Prime Factors

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


def isprime(n):
	if n==2 or n==3: 
		return True
	if n//2 == n/2:
		return False
	for i in range(2,int((n**0.5)+1),2):

		if n//i == n/i:
			return False
		else:
			return True


def factors(n):
#Calculate root n, loop over every value lower than that checking if it's a prime factor or not. 
	
	#initialise a list output

	a = []
	for i in range(2,int((n**0.5)+1)):
		if n/i == n//i:
			#add to list
			a.append(i)
			a.append(int(n/i))
	
	return a

	#return(n)


def primefactors(n):
#Calculate all roots, then cycle the list for factors.
	a = factors(n)
	return print(list(filter(isprime, a)))

	

#Particular question 
print(factors(13195))

print('-------')

print(factors(600851475143))

###Answer
#6857