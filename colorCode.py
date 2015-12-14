## STEPS: Read output/hierarchyclusterLOG
## catch each cluster as a list
## eliminate the largest cluster
## color code each cluster

##FUTURE: create as many colors as number of clusters
from collections import defaultdict

style = """<style type='text/css'>
html {
  font-family: Courier;
}
c0 {
	color: #000000;
}
c1 {
  color: #800000;
}
c2 {
  color: #00008B;
}
c3 {
  color: #0000CD;
}
c4 {
  color: #0000FF;
}
c5 {
  color: #006400;
}
c6 {
  color: #008000;
}
c7 {
  color: #008080;
}
c8 {
  color: #008B8B;
}
c9 {
  color: #00BFFF;
}
c10 {
  color: #00CED1;
}
c11 {
  color: #00FA9A;
}
c12 {
  color: #00FF00;
}
c13 {
  color: #00FF7F;
}
c14 {
  color: #00FFFF;
}
c15 {
  color: #191970;
}
c16 {
  color: #1E90FF;
}
c17 {
  color: #20B2AA;
}
c18 {
  color: #228B22;
}
c19 {
  color: #2E8B57;
}
c20 {
  color: #2F4F4F;
}
c21 {
  color: #32CD32;
}
c22 {
  color: #3CB371;
}
c23 {
  color: #40E0D0;
}
c24 {
  color: #4169E1;
}
c25 {
  color: #A52A2A;
}
c26 {
  color: #BA55D3;
}
c27 {
  color: #C71585;
}
</style>"""

clusters = defaultdict()

def write_html(f, type, str_):
    f.write('<%(type)s>%(str)s</%(type)s>' % {
            'type': type, 'str': str_ } )

def pickColor(i):
	if i==1:
		myCOLOR = 'c1'
	elif i==2:
		myCOLOR = 'c2'
	elif i==3:
		myCOLOR = 'c3'
	elif i==4:
		myCOLOR = 'c4'
	elif i==5:
		myCOLOR = 'c5'
	elif i==6:
		myCOLOR = 'c6'
	elif i==7:
		myCOLOR = 'c7'
	elif i==8:
		myCOLOR = 'c8'
	elif i==9:
		myCOLOR = 'c9'
	elif i==10:
		myCOLOR = 'c10'
	elif i==11:
		myCOLOR = 'c11'
	elif i==12:
		myCOLOR = 'c12'
	elif i==13:
		myCOLOR = 'c13'
	elif i==14:
		myCOLOR = 'c14'
	elif i==15:
		myCOLOR = 'c15'
	elif i==16:
		myCOLOR = 'c16'
	elif i==17:
		myCOLOR = 'c17'
	elif i==18:
		myCOLOR = 'c18'
	elif i==19:
		myCOLOR = 'c19'
	elif i==20:
		myCOLOR = 'c20'
	elif i==21:
		myCOLOR = 'c21'
	elif i==22:
		myCOLOR = 'c22'
	elif i==23:
		myCOLOR = 'c23'
	elif i==24:
		myCOLOR = 'c24'
	elif i==25:
		myCOLOR = 'c25'
	elif i==26:
		myCOLOR = 'c26'
	else:
		myCOLOR = 'c27'
	return myCOLOR



#write_html(f, RED, 'My name is so foo..\n')
#write_html(f, BLUE, '102838183820038.028391')

for line in open('output/hierarchyclusterLOG'):
	items = line.strip().split(" ")

	for item in items:
		try:
			if int(item):
				clusters[int(item)] = []
				i = int(item)
		except:
			clusters[i].append(item)
#print len(clusters)
f = open('out.html', 'w')
f.write('<html>')
f.write(style)

maxm=0
for i in xrange(len(clusters)):
	if maxm < len(clusters[i+1]):
		maxm = len(clusters[i+1])


for line in open('woPunctuation.txt'):
	items = line.strip().split(" ")
	for item in items:
		for i in xrange(len(clusters)):
			if item in clusters[i+1] and len(clusters[i+1]) != maxm:
				myCOLOR = pickColor(i)
				write_html(f, myCOLOR, item+" ")
			elif item in clusters[i+1] and len(clusters[i+1]) == maxm:
				myCOLOR = 'c0'
				write_html(f, myCOLOR, item+" ")









		