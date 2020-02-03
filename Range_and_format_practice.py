lst = []

for x in range(20):
  lst.append(x)

html_lst = []
for x in lst:
  html_lst.append('<li><h1>' + str(x) + '</h1></li>')

make_str = ''
for x in html_lst:
  make_str = make_str + x


x = '''<html>
  <head></head>
  <body>
    <ul>
      <li>
        <h1>
          {0}
        </h1>
      </li>
    </ul>
  </body>
</html>'''

print( x.format(make_str) )