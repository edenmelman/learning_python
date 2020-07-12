def find_first_unique_ind(string):
	
	char_ind_list = [None] * 26

	for ind in range(len(string)):
		char_cell = ord(string[ind]) - 97

		if char_ind_list[char_cell] == None:
			char_ind_list[char_cell] = ind

		else:
			char_ind_list[char_cell] = -1

	final_ind_list = [ind for ind in char_ind_list if ind != None and ind != -1]

	if final_ind_list:
		return(min(final_ind_list))
	return -1
