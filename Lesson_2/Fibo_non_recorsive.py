def fibo_test():
	"""[0,1,1,2,3,5,8]"""
	result = fibo(5)
	if result == 3:
		print("great success")
	else:
		print("you are a loser")
		print(result)
		

def fibo(ele_input):
	m = 1
	n = 0
	ele = 2
	if ele_input == 1:
		return n
	if ele_input == 2: 
		return m
	while  ele < ele_input:
		m = m + n
		n = m - n
		ele += 1
	return m

fibo_test()

#0,1,1,2,3,5,8

def fibo(n):
	b = 1
	a = 0
	if n == 1:
		return a
	if n == 2: 
		return b
	for _ in range(3,n+1):
		a, b = b, b + a
		
	return b