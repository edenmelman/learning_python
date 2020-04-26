expected = ["1","2","Fizz","4","5","Fizz","Buzz","8","Fizz","10","11","Fizz","Fizz","Buzz","Fizz","16","Buzz","Fizz","19","20","FizzBuzz"]

result = []
n = 21
for num in range(1,n+1):
	if (num % 3 == 0 and num % 7 == 0) or ("3" in str(num) and "7" in str(num)):
		result.append("FizzBuzz")
	elif num % 3 == 0 or "3" in str(num):
		result.append("Fizz")
	elif num % 7 == 0 or "7" in str(num):
		result.append("Buzz")
	else:
		result.append(str(num))


if result == expected:
	print("Great Success")
else:
	print("you are a loser")
	print(expected)
	print(result)
