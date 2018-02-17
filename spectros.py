import secrets

version = "0.0.0"
print("Spectros v" + version);

def information(n):
	"""Return random bits"""
	return secrets.randbits(n)

def de2bi(n):
	"""Transform a base 10 integer in a base 2 integer"""
	bits = []
	if (n == 1):
		bits = [1]
	if (n == 0):
		bits = [0]
	while (n > 1):
		bits.insert(0, n%2)
		n //= 2
		if (n == 1):
			bits.insert(0, 1)
	return bits
	
print(information(10))
print(de2bi(127))
