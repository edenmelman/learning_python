def reveal_message(message):
	max_ind = len(message)-1

	for ind in range(max_ind,-1,-1):
		if message[ind] == ' ':
			for i in range(ind,max_ind):
		 		message.append(message.pop(ind+1))
			message.append(message.pop(ind))
			max_ind = ind - 1

	for ind in range(0,max_ind+1):
		message.append(message.pop(0))
		