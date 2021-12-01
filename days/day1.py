from util.DayModel import DayModel


class Day1(DayModel):
	input_is_int = True

	example_data = [
		199,
		200,
		208,
		210,
		200,
		207,
		240,
		269,
		260,
		263
	]
	example_expected_result_1 = 7
	example_expected_result_2 = 5

	def calc(self):
		self.result_part_1 = sum(x < y for x, y in zip(self.input_data, self.input_data[1:]))
		self.result_part_2 = sum(x < y for x, y in zip(self.input_data, self.input_data[3:]))
