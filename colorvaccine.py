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

numvaccine = 0
for line in open('FILES/words_cluster.txt'):
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

f = open('FILES/vaccine.html', 'w')
f.write('<html>')
f.write(style)

for line in open('FILES/vaccine.txt'):
	items = line.strip().split(" ")
	for item in items:
		if item in clusters[numvaccine]:
			write_html(f,'c1', item+' ')
		else:
			write_html(f, 'c0', item+' ')
		