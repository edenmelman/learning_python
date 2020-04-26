def test_binary():
	result_test_1 = binary_search(3,[])
	assert result_test_1  == False, 'for (3,[])- I expected to get False, but the function returned {}'.format(result_test_1)

	result_test_2 = binary_search(4,[1,2,3,4])
	assert result_test_2 == True, 'for (4,[1,2,3,4]) - I expected to get True but the function returned {}'.format(result_test_2)

	result_test_5 = binary_search(10,[1,2,3,4,5,6,7,10])
	assert result_test_5 == True, 'for (10,[1,2,3,4,5,6,7,10]) - I expected to get True but the function returned {}'.format(result_test_5)

	result_test_6 = binary_search(3,[1,2,3,4,5,6,7,10])
	assert result_test_6 == True, 'for (10,[1,2,3,4,5,6,7,10]) - I expected to get True but the function returned {}'.format(result_test_6)

	result_test_3 = binary_search(0,[1,2,3,5,10])
	assert result_test_3 == False, 'for (0,[1,2,3,5,10]) - I expected to get True but the function returned {}'.format(result_test_3)

	result_test_4 = binary_search(1,[1])
	assert result_test_4 == True, 'for (1,[1]) - I expected to get True but the function returned {}'.format(result_test_4)

	print("Great Success")

def binary_search(num,l):

	if len(l) == 0:
		return False

	ref_ind = len(l) // 2

	if num == l[ref_ind]:
		return True

	if num > l[ref_ind]:
		l = l[ref_ind + 1 : len(l)]
		#print (l)
		is_there = binary_search(num,l)
		return is_there

	else:
		l = l[0 : ref_ind]
		#print(l)
		is_there = binary_search(num,l)
		return is_there

test_binary()


#Comments:
# if not l >> if len(l)==0 || because the first will support no list at all.
# [1,2,3,4,5,6,7,8,9,10]
# [6,7,8,9,10]
