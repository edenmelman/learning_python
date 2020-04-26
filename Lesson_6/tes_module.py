from module import f

def test_if_f_is_valid():
	assert f() == True

def test_if_f_is_invalid():
	assert f() == False
