def is_prime(x):
    """A function that generates prime numbers from 0 to n"""
    from math import sqrt
    num = 2
    if x < 2:
        print ("The first prime number is 2!")
        return False
        while True:
            if num <= sqrt(x):
                if (x % num) == 0:
                    return False
            else:
                num += 1
                return True
		num_prime = []
		for i in range(2, (n + 1)):
			if is_prime(i):
				num_prime.append(i)
	

		return num_prime

