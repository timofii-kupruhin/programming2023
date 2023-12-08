# Залік з програмування Купрюхін Тимофій КІ-2

class Programm():
	def __init__(self, file_name):
		self.__FILE_NAME = file_name

	def read_file(self):
		with open(self.__FILE_NAME, "r") as f:
			file_data = f.readlines()
		return file_data

	def collect_data(self):
		user_input = input("Write your word (!q-quit): ")
		if user_input == "!q":
			exit()
		return user_input

	def search_user_input(self):
		file_data = self.read_file()
		user_input = self.collect_data()
		result = []
		if file_data:
			for line in file_data:
				if user_input in line:
					result += [file_data.index(line)]
		return result

prog = Programm("test.txt")


if __name__ == "__main__":
	while 1:
		indexes_lst = prog.search_user_input()
		file_data = prog.read_file()
		if indexes_lst:
			print("Your word was found in: " + ", ".join([str(index+1) for index in indexes_lst]) + " lines")
			print("\n".join([file_data[index].replace('\n', '') for index in indexes_lst]))
		else:
			print("Your word was not found !!")
		print()