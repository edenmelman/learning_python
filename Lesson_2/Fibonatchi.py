def fibo_test():
	"""[0,1,1,2,3,5,8]"""
	result = fibo(5,{})
	if result == 3:
		print("great success")
	else:
		print("you are a loser")
		print(result)

def fibo(n,d):
	if n == 1:
		return 0
	if n == 2:
		return 1
	return fibo(n-2)+fibo(n-1)


fibo_test()