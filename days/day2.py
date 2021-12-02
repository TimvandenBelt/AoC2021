from util.DayModel import DayModel


class Day2(DayModel):
	day = 2

	example_data = [
		"forward 5",
		"down 5",
		"forward 8",
		"up 3",
		"down 8",
		"forward 2",
	]
	example_expected_result_1 = 150
	example_expected_result_2 = 900

	def calc(self):
		x = 0
		y = 0
		y2 = 0
		aim = 0
		for action_text in self.input_data:
			action_data = action_text.split(" ")
			action = action_data[0]
			amount = int(action_data[1])
			match action:
				case "forward":
					x += amount
					y2 += aim * amount
				case "down":
					y -= amount
					aim -= amount
				case "up":
					y += amount
					aim += amount

		self.result_part_1 = abs(x * y)
		self.result_part_2 = abs(x * y2)
