import random

upper_bound = raw_input("Guess a number between 1 and _____ (pick a number)")

n = random.randint(1, int(upper_bound))
#print n

def guess_number(w):
	if w > n:
		print "guess too high"
	elif w < n:
		print "guess too low"
	else:
		print "you win!"

number = float(raw_input("Guess a number:"))
print number
	
guess_number(number)

while (number!=n):
	number = float(raw_input ("Guess another number"))
	guess_number(number)
