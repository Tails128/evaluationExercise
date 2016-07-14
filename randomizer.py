import random;

pizze = ["margherita","marinara","quattro stagioni", "capricciosa" , "viennese","tonno","salamino","patatine"];
aggiunte = ["formaggio","pomodoro","olio piccante","funghi","tonno","wurstel","salamino","patatine","peperoni","bufala"];

for i in range(10000):	#randomizes 10000 pizza(s)
	base = random.randrange(0,len(pizze));		#pizza's base
	addon =["","",""];							#max 3 addons
	randomized=random.randrange(0,4);
	if randomized < 3:							#randomize pizza's addons with a 75% possibility of addons
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
	else:
		print(pizze[base]);