import fileinput

indexAdding = 0			#idMachine's position
indexTotal = 1				#downtime's position
currentindex = 'capricciosa'			#starting index
total = 0					#total addings


for line in fileinput.input():			#each line's read and split
	values = line.split('\t');
	pizzaID = values[indexAdding];
	if(pizzaID != currentindex):		#if machineID is not equal to current 
		print(('{0}\t{1}'.format(currentindex, total)).replace("\n",""))	#print summed downtime
		currentindex = pizzaID;											#and initialize to the new index
		total = 0;
	total += int(values[indexTotal].replace("\n",""))						#add the current downtime
print(('{0}\t{1}'.format(currentindex, total)).replace("\n",""))			#final print