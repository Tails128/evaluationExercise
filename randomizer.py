import random;

pizze = ["margherita","marinara","quattro stagioni", "capricciosa" , "viennese","tonno","salamino","patatine"];
aggiunte = ["formaggio","pomodoro","olio piccante","funghi","tonno","wurstel","salamino","patatine","peperoni","bufala"];

for i in range(10000):
	base = random.randrange(0,len(pizze));
	addon =["","",""];
	randomized=random.randrange(0,2);
	if randomized == 1:
		howMany = random.randrange(0,3);
		start = 0;
		while(start <= howMany):
			addon[start] = random.randrange(0,len(aggiunte));
			start += 1;
		addonString = "";
		for i in range(3):
			if(addon[i]!= ""):
				if(i==0):
					addonString +=aggiunte[int(addon[i])];
				else:
					addonString += ' , {0}'.format(aggiunte[int(addon[i])]);
		print(('{0} + {1}'.format(pizze[base], addonString)));
#	else:
#		print(pizze[base]);