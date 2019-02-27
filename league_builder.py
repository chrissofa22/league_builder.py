import csv

def opener(data):
	with open(data, newline='') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',')
		info = list(reader)
	return info

if __name__ == "__main__":
	info = opener("soccer_players.csv")
	y = []
	n = []
	for section in info:
		if section['Soccer Experience'] == 'YES':
			y.append(section)
		else:
			n.append(section)

	n1 = n[:3]
	n2 = n[3:6]
	n3 = n[6:9]
	y1 = y[:3]
	y2 = y[3:6]
	y3 = y[6:9]
	s = n1 + y1
	d = n2 + y2
	r = n3 + y3

	with open("teams.txt", "w") as file:
		file.write("Sharks:\n\n")
		for member in s:
			file.write("{Name}, {Soccer Experience}, "
				"{Guardian Name(s)}\n".format(**member))
		file.write("\nDragons:\n\n")
		for member in d:
			file.write("{Name}, {Soccer Experience}, "
				"{Guardian Name(s)}\n".format(**member))
		file.write("\nRaptors:\n\n")
		for member in r:
			file.write("{Name}, {Soccer Experience}, "
				"{Guardian Name(s)}\n".format(**member))

	for member in s:
		member["Team"] = "Sharks"
	for member in d:
		member["Team"] = "Dragons"
	for member in r:
		member["Team"] = "Raptors"

	update = s + d + r

	for member in update:
		name = "_".join(member["Name"].lower().split()) + ".txt"
		with open(name, "w") as file:
			file.write("Hello {Guardian Name(s)}!\n\n".format(**member))
			file.write("{Name} will be put onto the\n"
				"team {Team}. The {Team} will meet together\n"
				"Friday, March 22 at 11:30am. Get ready to\n"
        		"kick some soccer butt!\n".format(**member))
