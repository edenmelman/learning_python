def test_binary():
	result_test_1 = False
	assert result_test_1  == False, 'for (3,[])- I expected to get False, but the function returned {}'.format(result_test_1)

	result_test_2 = False
	assert result_test_2 == True, 'for (4,[1,2,3,4]) - I expected to get True but the function returned {}'.format(result_test_2)

test_binary()