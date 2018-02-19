import secrets
import matplotlib.pyplot as plt
import numpy as np

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
	
def sinus(min=0, max=2*np.pi, prec=1000):
	result = []
	time = np.linspace(min, max, prec)
	result = np.sin(time)
	return [time , result] 

vals = sinus(-10*np.pi, 10*np.pi, 10**3)
plt.plot(vals[0], vals[1])
plt.show()
	
