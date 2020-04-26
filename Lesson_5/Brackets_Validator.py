def test_validator():
	result_test_1 = Brackets_Validator("{}")
	assert result_test_1 == True, 'for ("/{}/"") Result should be True, but was %s'%(result_test_1)

	result_test_2 = Brackets_Validator("{[]}")
	assert result_test_2 == True, 'for ("{[]}") Result should be True, but was %s'%(result_test_2)

	result_test_3 = Brackets_Validator("{[}]")
	assert result_test_3 == False, 'for ("{[}]") Result should be False, but was %s'%(result_test_3)

	result_test_4 = Brackets_Validator("{(]])}")
	assert result_test_4 == False, 'for ("{(]])}") Result should be False, but was %s'%(result_test_4)

	result_test_5 = Brackets_Validator("[{}")
	assert result_test_5 == False, 'for ("[{}") Result should be False, but was %s'%(result_test_5)

	result_test_6 = Brackets_Validator("{(([{}]))}")
	assert result_test_6 == True, 'for ("{(([{}]))}") Result should be False, but was %s'%(result_test_6)

	result_test_7 = Brackets_Validator("{r(([{}s]))ff}")
	assert result_test_7 == True, 'for ("{r(([{}s]))ff}") Result should be False, but was %s'%(result_test_7)


	print("Great Success")



def Brackets_Validator(a):
	Brackets_dict = {"{":"}","[":"]","(":")"}
	Brackets_stack = [] 

	for b in (a):
		if b in Brackets_dict:
			Brackets_stack.append(b)
			#print(Brackets_stack)

		if b in Brackets_dict.values():
			if b == Brackets_dict[Brackets_stack[-1]]:
				Brackets_stack.pop()
				#print(Brackets_stack)
			else:
				return False

	if len(Brackets_stack) != 0:
		return False
	else:
		return True

#Brackets_Validator("{(]])}")

test_validator()
