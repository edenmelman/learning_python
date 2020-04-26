def swap_specific_word(message,first_ind,last_ind):
	num_of_swaps = (last_ind + 1 - first_ind) // 2
	
	for _ in range(num_of_swaps):
		message[first_ind], message[last_ind] = message[last_ind], message[first_ind]

		first_ind += 1
		last_ind -= 1
		

def reveal_message(message):
	min_ind = 0
	max_ind = len(message)

	while ' ' in message[min_ind:]:
		space_ind = message.index(' ',min_ind)
		swap_specific_word(message,min_ind,space_ind -1)

		min_ind = space_ind + 1
	
	swap_specific_word(message,min_ind,max_ind-1)

