import os
import doors

def clear():
	os.system('clear||cls')

def menu(codes_list):
	clear()
	i = 0
	for p in codes_list:
		i = i + 1
		print(str(i) + ' - ' + p)
	c_id = int(input('> '))
	while c_id <= 0 or c_id >= len(codes_list) + 1:
		print('Wrong input !')
		c_id = int(input('> '))
	print('')
	launch_code(c_id)

def launch_code(c_id):
	if c_id == 1:
		doors.main()
	print('\nCode finished executing !')

if __name__ == '__main__':
	codes_list = ['100 doors']
	menu(codes_list)