Def generate_prime(n):
		"""A function that generates prime numbers from 0 to n"""
		def is_prime(x):
	
	
	from math import sqrt
	

			num = 2
	

			if x < 2:
				print "The first prime number is 2!"
				return False
	

			while True:
				if num <= sqrt(x):
					if (x % num) == 0:
						return False
					else:
						num += 1
				else:
					return True
