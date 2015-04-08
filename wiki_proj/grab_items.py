
import re
infoboxes = []

with open("examples_latd+infobox.xml") as f:
	box_s = ''
	state = False
	opens = 0
	closes = 0
	for line in f:
		if (state == False):
			if ("{{Infobox"  in line):
				opens += 1
				attr = line[10:]
				attr = attr.rstrip()
				box_s += '<infobox ' + 'class="'+attr +'">\n' + line
				state = True
				continue

#START COLLECTING
		if (state):
			opens += line.count("{{")
			closes += line.count("}}")
			box_s += line
			#print(opens, closes)
			if (opens == closes):
				infoboxes.append(box_s + '</infobox>')
				state = False

for line in infoboxes:
	print(line)
			