def find_first_unique_ind(string):
	char_dict = {}
	for ind in range(len(string)):
		if string[ind] in char_dict:
			char_dict[string[ind]] = -1
		else:
			char_dict[string[ind]] = ind
	ind_list = list(char_dict.values())
	ind_list.sort()
	for ind in ind_list:
		if ind!= -1:
			return ind
	return -1