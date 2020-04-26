def fibo_test():
	"""[0,1,1,2,3,5,8]"""
	result = fibo(5)
	if result == 3:
		print("great success")
	else:
		print("you are a loser")
		print(result)

def fibo(n,fib_memo = {1:0,2:1}):
	if n in fib_memo.keys():
		print("used exsisting")
		return fib_memo[n]
	fib_memo[n] = fibo(n-2)+fibo(n-1)
	print(fib_memo)
	return fib_memo[n]


fibo_test()

def fibo(n,fib_memo=None):
	if not fib_memo:
		fib_memo = {1: 0, 2: 1}

	if n not in fib_memo:
		fib_memo[n] = fibo(n-2, fib_memo) + fibo(n-1, fib_memo)
	return fib_memo[n]