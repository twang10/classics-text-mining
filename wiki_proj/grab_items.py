
import re
infoboxes = []

with open("examples_latd+infobox.xml") as f:
	box_s = ''
	in_itembox = False
	has_locs = False
	opens = 0
	closes = 0
	for line in f:
		if (state == False):
			if ("{{Infobox"  in line ): #(and "settlement" in line):
				opens += 1
				attr = line[10:]
				attr = attr.rstrip()
				box_s += '<infobox ' + 'class="'+attr +'">\n' + line
				in_itembox = True
				continue

		#START COLLECTING
		if (state):
			opens += line.count("{{")
			closes += line.count("}}")
			box_s += line
			if('latd' in line):
				has_locs = True
			#print(opens, closes)

			#TODO: -look for latd and longd in line
			if (opens == closes):
				if has_locs:
					infoboxes.append(box_s + '</infobox>')
				has_locs = False
				in_itembox = False

for line in infoboxes:
	print(line)
			
