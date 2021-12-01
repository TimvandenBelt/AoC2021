import fileinput


def file_to_array(file_location, parse_as_int=False):
	with fileinput.input(files=file_location) as fileInput:
		lines = []
		for line in fileInput:
			line = line.rstrip("\n")
			if parse_as_int:
				line = int(line)
			lines.append(line)
		return lines
