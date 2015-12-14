style = """<style type='text/css'>
html {
  font-family: Courier;
}
r {
  color: #ff0000;
}
g {
  color: #00ff00;
}
b {
  color: #0000ff;
}
</style>"""

RED = 'r'
GREEN = 'g'
BLUE = 'b'

def write_html(f, type, str_):
    f.write('<%(type)s>%(str)s</%(type)s>' % {
            'type': type, 'str': str_ } )

f = open('out.html', 'w')
f.write('<html>')
f.write(style)

write_html(f, RED, 'My name is so foo..\n')
write_html(f, BLUE, '102838183820038.028391')

f.write('</html>')

