from util.DayModel import DayModel


def compare_bit_from_row(row_string, bit_index, bit_value):
	if int(row_string[bit_index]) == bit_value:
		return True
	return False


def parse_bit_char(bit, column_index, total_val_per_bit_column):
	bit = int(bit)
	if column_index <= len(total_val_per_bit_column) - 1:
		total_val_per_bit_column[column_index] += -1 if bit == 0 else 1
	else:
		total_val_per_bit_column.append(-1 if bit == 0 else 1)


def binary_to_decimal(co2, epsilon, gamma, oxygen):
	gamma_decimal = int(gamma, 2)
	epsilon_decimal = int(epsilon, 2)
	co2_decimal = int(co2, 2)
	oxygen_decimal = int(oxygen, 2)
	return co2_decimal, epsilon_decimal, gamma_decimal, oxygen_decimal


def parse_bit_rows(input_data, total_val_per_bit_column):
	row_index = 0
	for bits_row_string in input_data:
		column_index = 0
		loop_val = bits_row_string
		for bit in loop_val:
			parse_bit_char(bit, column_index, total_val_per_bit_column)
			column_index += 1
		row_index += 1


def get_search_bit(bit_position, total_val_per_bit_column, is_oxygen_rating):
	total_val_of_bit_column = total_val_per_bit_column[bit_position]

	if total_val_of_bit_column == 0:
		return 1 if is_oxygen_rating else 0
	if total_val_of_bit_column > 0:
		return 1 if is_oxygen_rating else 0
	return 0 if is_oxygen_rating else 1


class Day3(DayModel):
	day = 3

	example_data = [
		"00100",
		"11110",
		"10110",
		"10111",
		"10101",
		"01111",
		"00111",
		"11100",
		"10000",
		"11001",
		"00010",
		"01010"
	]
	example_expected_result_1 = 198
	example_expected_result_2 = 230

	def calc(self):
		total_val_per_bit_column = []
		parse_bit_rows(self.input_data, total_val_per_bit_column)

		gamma = ""
		epsilon = ""
		char_pos_index = 0
		for total_val in total_val_per_bit_column:
			gamma += str(get_search_bit(char_pos_index, total_val_per_bit_column, is_oxygen_rating=True))
			epsilon += str(get_search_bit(char_pos_index, total_val_per_bit_column, is_oxygen_rating=False))
			char_pos_index += 1

		oxygen = self.recursive(self.input_data, total_val_per_bit_column)
		co2 = self.recursive(self.input_data, total_val_per_bit_column, is_oxygen_rating=False)

		co2_decimal, epsilon_decimal, gamma_decimal, oxygen_decimal = binary_to_decimal(co2, epsilon, gamma, oxygen)

		self.result_part_1 = gamma_decimal * epsilon_decimal
		self.result_part_2 = co2_decimal * oxygen_decimal

	def recursive(self, array, total_val_per_bit_column, bit_position=0, is_oxygen_rating=True):
		result = []

		looking_for_bit = get_search_bit(bit_position, total_val_per_bit_column, is_oxygen_rating)

		for bit_string_row in array:
			if compare_bit_from_row(bit_string_row, bit_position, looking_for_bit):
				result.append(bit_string_row)

		if len(result) == 1:
			return result[0]

		if len(result) == 0:
			result = array

		new_total_val_per_bit_column = []
		parse_bit_rows(result, new_total_val_per_bit_column)

		return self.recursive(result, new_total_val_per_bit_column, bit_position + 1, is_oxygen_rating)
