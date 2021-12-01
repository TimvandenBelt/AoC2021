from abc import ABC, abstractmethod


class AbstractDay(ABC):

	@property
	def day(self):
		return

	@property
	def path_to_input_file(self):
		return

	@property
	def input_data(self):
		return

	@property
	def input_is_int(self):
		return

	@property
	def example_data(self):
		return

	@property
	def example_expected_result_1(self):
		return

	@property
	def example_expected_result_2(self):
		return

	@property
	def result_part_1(self):
		return

	@property
	def result_part_2(self):
		return

	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def set_input(self, value):
		pass

	@abstractmethod
	def get_input_from_file(self):
		pass

	@abstractmethod
	def test(self):
		pass

	@abstractmethod
	def calc(self):
		pass

	@abstractmethod
	def print_result(self, value, part=1):
		pass

	@abstractmethod
	def print_test_success(self):
		pass

	@abstractmethod
	def print_failed_tests(self, objects):
		pass

	@abstractmethod
	def part_1(self):
		pass

	@abstractmethod
	def part_2(self):
		pass
