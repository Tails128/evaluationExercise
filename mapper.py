#!/usr/bin/python
import fileinput

indexIdMachine = 2		#field IDMachine's position
indexDowntime = 3		#field downtime's position

for line in fileinput.input():				#read and split of the csv
	values = line.split('+')
	if(len(values) ==2):
		addons = values[1].split(',');
		for value in addons:
			tempVal = value.replace('\n','');
			tempVal = tempVal.replace(' ','');
			print('{0}\t1'.format(tempVal));