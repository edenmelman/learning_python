def test_validator():
	result_test_1 = validate_brackets("{}")
	assert result_test_1 == True, 'for ("/{}/"") Result should be True, but was %s'%(result_test_1)

	result_test_2 = validate_brackets("{[]}")
	assert result_test_2 == True, 'for ("{[]}") Result should be True, but was %s'%(result_test_2)

	result_test_3 = validate_brackets("{[}]")
	assert result_test_3 == False, 'for ("{[}]") Result should be False, but was %s'%(result_test_3)

	result_test_4 = validate_brackets("{(]])}")
	assert result_test_4 == False, 'for ("{(]])}") Result should be False, but was %s'%(result_test_4)

	result_test_5 = validate_brackets("[{}")
	assert result_test_5 == False, 'for ("[{}") Result should be False, but was %s'%(result_test_5)

	result_test_6 = validate_brackets("{(([{}]))}")
	assert result_test_6 == True, 'for ("{(([{}]))}") Result should be True, but was %s'%(result_test_6)

	result_test_7 = validate_brackets("{(([{}]))}")
	assert result_test_7 == True, 'for ("{(([{}]))}") Result should be True, but was %s'%(result_test_7)

	result_test_8 = validate_brackets("{}[]()")
	assert result_test_8 == True, 'for ("{}[]()") Result should be True, but was %s'%(result_test_8)


	print("Great Success")



def validate_brackets(string):
	brackets_map = {"{":"}","[":"]","(":")"}
	stack = [] 

	for char in string:
		if char in brackets_map:
			stack.append(char)
			#print(stack)

		elif char in brackets_map.values():
			if char != brackets_map[stack.pop()]:
				return False
				
	if stack:
		return False
	return True


test_validator()
