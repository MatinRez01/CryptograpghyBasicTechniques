# Python program for the extended Euclidean algorithm

def exGcd(a,b):
	if b == 0:
		return [1, 0]
	r = a%b
	[x, y] = exGcd(b, r)
	n = a//b
	return [y, x - n*y]
 
if __name__ == '__main__':
 
    x, y = exGcd(35, 20)
  #  print('The GCD is', gcd)
    print(f'x = {x}, y = {y}')
    print(f'{pow(11, 1) % 29}')