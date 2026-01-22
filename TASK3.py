user_file = input("input file name: ")

try:
	file = open(user_file, "r")
except FileNotFoundError: 
	print("file does not exist")
except PermissionError:
	print("no permission to read")
except IOError as e:
	print(e)
else: 
	line_count = 0
	for line in file: 
		line_count += 1
	print("number of lines:", line_count)

	word_count = 0
	for word in file:
		word_count += 1
	print("number of words:", word_count)

	char_count = 0
	for characters in file:
		char_count += 1
	print("number of characters:", char_count)
finally:
	file.close()

	
	
		
	
