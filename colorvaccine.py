from collections import defaultdict

style = """<style type='text/css'>
html {
  font-family: Courier;
}
c0 {
	color: #000000;
}
c1 {
  color: #33FF00;
}
</style>"""

clusters = defaultdict()

def write_html(f, type, str_):
    f.write('<%(type)s>%(str)s</%(type)s>' % {
            'type': type, 'str': str_ } )


#write_html(f, RED, 'My name is so foo..\n')
#write_html(f, BLUE, '102838183820038.028391')
numvaccine = 0
for line in open('outputbluemix/hierarchyclusterLOG'):
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
#print len(clusters)
f = open('outputbluemix/vaccine.html', 'w')
f.write('<html>')
f.write(style)

print numvaccine
print clusters

for line in open('vaccine_bluemix_processed.txt'):
	items = line.strip().split(" ")
	for item in items:
		if item in clusters[numvaccine]:
			write_html(f,'c1', item+' ')
		else:
			write_html(f, 'c0', item+' ')






		








		