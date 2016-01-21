from collections import defaultdict

clusters = defaultdict()
numvaccine = 0
for line in open('FILES/words_cluster.txt'):
	line = line.replace('........','')
	line = line.replace('cluster: ','')
	items = line.strip().split(" ")

	for item in items:
		try:
			if int(item):
				clusters[int(item)] = []
				i = int(item)
		except:
			clusters[i].append(item)
			if item == 'vaccine':
				numvaccine = i

medical_time = 0.0
tempmed = 0.0
#non_medical_time = 0.0
total_time = 0.0
mylist = []

for line in open('FILES/vaccine.csv'):
	items = line.strip().split(",")
	if items[0] == "WORD":
		continue
	if items[0] in clusters[numvaccine]:
		#print len(mylist)
		#print "+++++++++++++++++++"
		for item in mylist:
			if len(mylist) > 100:
				tempmed = 0.0
				break
			tempmed += float(item[1])

		mylist = []
		medical_time += float(tempmed)
	else:
		mylist.append([items[0], items[2]])
		#non_medical_time += float(items[2])
	total_time += float(items[2])

print "Time in minutes (just based on clusters) medical_time, non_medical_time, total_time"
#print medical_time/60., non_medical_time/60., total_time/60.
print medical_time/60., total_time/60.

print "Percentage of medical converstaion: "
print float(medical_time/total_time)*100.