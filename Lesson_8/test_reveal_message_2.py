from reveal_message import reveal_message

def test_no_spaces():
	message = ['o','l','l','e','h']
	reveal_message(message)
	assert message == ['o','l','l','e','h']

def test_classic():
	message = ['g','e','o','r','g','i','o',' ','l','a','t','e','r',' ','y','o','u',' ','s','e','e',' ','b','e','y',' ','h','e','y']
	reveal_message(message)
	assert message == ['h','e','y',' ','b','e','y',' ','s','e','e',' ','y','o','u',' ','l','a','t','e','r',' ','g','e','o','r','g','i','o']

def test_one_letter_each_word():
	message = ['o',' ','l',' ','h']
	reveal_message(message)
	assert message == ['h',' ','l',' ','o']

def test_two_words():
	message = ['o', 'k', 'a', 'y',' ','n', 'o','t']
	reveal_message(message)
	assert message == ['n','o','t',' ','o','k','a','y']