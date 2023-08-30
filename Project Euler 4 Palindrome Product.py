#Project Euler 4 Palindrome Product

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def ispalindrome(n):
	a = str(n)
	out = 0
	for i in range(0,len(a)//2):
		if not a[i]==a[len(a)-i-1]:
			out = out +1
	if out == 0:
		return True
	else:
		return False

def large3digmul(n):
	a = 999
	b = 999
	c = []
	for i in range(0,n):
		d=a-i
		for i in range(0,n):
			e=b-i
			c.append(d*e)
	return(c)




#Specific Question

#Find the largest palindrome made from the product of two 3-digit numbers.
a=large3digmul(100)

print(list(filter(ispalindrome, a)))

#Output = [906609, 886688, 888888, 861168, 888888, 861168, 886688, 824428, 906609, 819918, 824428, 819918]

#Answer
#906609


#Reflection: I dislike having a double for loop in def large3digmul here. 
#It seems most online solutions do solve it similarly, but something that could speed it up is that all palindromes with even digit numbers are divisible by 11.