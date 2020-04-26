def swap_specific_word(message,first_ind,last_ind):
	while (last_ind > first_ind):
		message[first_ind], message[last_ind] = message[last_ind], message[first_ind]
		
		first_ind += 1
		last_ind -= 1
		

def reveal_message(message):
	min_ind = 0
	words_dict = {}

	while ' ' in message[min_ind:]:
		space_ind = message.index(' ',min_ind)
		words_dict[min_ind] = space_ind - 1

		min_ind = space_ind + 1

	words_dict[min_ind] = len(message) - 1

	for key in words_dict:
		swap_specific_word(message,key,words_dict[key])

