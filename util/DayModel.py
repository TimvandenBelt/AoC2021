from colorama import init, Fore, Style
from util import file
from util.AbstractDay import AbstractDay

init(autoreset=True)


class DayModel(AbstractDay):
	day = 1
	input_data = None
	result_part_1 = None
	result_part_2 = None
	input_is_int = False
	example_data = []
	example_expected_result_1 = 0
	example_expected_result_2 = 0

	def __init__(self):
		print(Fore.YELLOW + "========= " + Fore.WHITE + Style.BRIGHT + "BEGIN DAY {} ".format(self.day) + Fore.YELLOW + Style.NORMAL + "=========")
		self.test()
		self.set_input(self.get_input_from_file())
		self.calc()
		self.part_1()
		self.part_2()
		print(Fore.YELLOW + "========= " + Fore.WHITE + Style.BRIGHT + "END DAY {} ".format(self.day) + Fore.YELLOW + Style.NORMAL + "=========")

	def set_input(self, value):
		self.input_data = value

	def get_input_from_file(self):
		return file.file_to_array(file_location='./inputs/inputday{}'.format(self.day), parse_as_int=self.input_is_int)

	def test(self):
		self.set_input(self.example_data)
		self.calc()
		if self.example_expected_result_1 == self.result_part_1 and self.example_expected_result_2 == self.result_part_2:
			self.print_test_success()
		else:
			self.print_failed_tests([self.result_part_1, self.result_part_2])
		self.result_part_1 = None
		self.result_part_2 = None

	def calc(self):
		pass

	def print_result(self, value, part=1):
		if value:
			print('Day {} - part {} result: {}'.format(self.day, part, value))
		else:
			print("Day {} - part {} result: \033[31mfailed\033[0m".format(self.day, part))

	def print_test_success(self):
		print("Day {} - test: \033[32msuccess\033[0m".format(self.day))

	def print_failed_tests(self, objects=None):
		if objects is None:
			objects = []
		print('Day {} test: \033[31mfailed\033[0m'.format(self.day))
		for object_value in objects:
			print('Received: {}'.format(object_value))

	def part_1(self):
		self.print_result(self.result_part_1)

	def part_2(self):
		self.print_result(self.result_part_2, part=2)
