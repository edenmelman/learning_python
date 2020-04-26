from secret_message import reveal_message,swap_specific_word

def test_no_spaces():
	message = ['o','l','l','e','h']
	reveal_message(message)
	assert message == ['h','e','l','l','o']


def test_classic_with_odd_num_of_char_in_each_word():
	message = ['y','e','h',' ','y','e','b',' ','e','e','s',' ','u','o','y',' ','r','e','t','a','l',' ','o','i','g','r','o','e','g']
	reveal_message(message)
	assert message == ['h','e','y',' ','b','e','y',' ','s','e','e',' ','y','o','u',' ','l','a','t','e','r',' ','g','e','o','r','g','i','o']


def test_classic_with_even_num_of_char_in_each_word():
	message = ['t','r','e','b','l','a',' ','s','e','i','g','o','l','o','n','h','c','e','t',' ','k','c','o','r']
	reveal_message(message)
	assert message == ['a','l','b','e','r','t',' ','t','e','c','h','n','o','l','o','g','i','e','s',' ','r','o','c','k']

def test_one_char_each_word():
	message = ['r',' ','u',' ','k',' ','?']
	reveal_message(message)
	assert message == ['r',' ','u',' ','k',' ','?']

def test_starts_and_ends_with_a_space():
 	 message = [' ','n','o','b',' ','e','t','i','t','e','p','p','a',' ']
 	 reveal_message(message)
 	 assert message == [' ','b','o','n',' ','a','p','p','e','t','i','t','e',' ']

 #def test_only_one_space():
 	#message = [' ']
 	#reveal_message(message)
 	#assert message == [' ']

 #def test_2_spaces_no_word():
 	#message = [' ',' ']
 	#reveal_message(message)
 	#assert message = [' ',' ']