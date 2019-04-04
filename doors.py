def run():
	doors_open = []
	doors_close = []
	doors_list = [1 for i in range(100)]
	i = 1
	while i < len(doors_list):
		if doors_list[i] == 0:
			doors_list[i] = 1
		else:
			doors_list[i] = 0
		i += 2
	i = 2
	while i < len(doors_list):
		if doors_list[i] == 0:
			doors_list[i] = 1
		else:
			doors_list[i] = 0
		i += 3
	i = 0
	while i < len(doors_list):
		if doors_list[i] == 0:
			doors_open.append(i + 1)
		else:
			doors_close.append(i + 1)
		i += 1
	print('Doors open : \n')
	for p in doors_open:
		print(p)
	print('\nDoors closed : \n')
	for p in doors_close:
		print(p)

class main(object):
	def __init__(self):
		run()