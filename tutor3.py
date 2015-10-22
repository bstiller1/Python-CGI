#!C:\Users\triosStudent\AppData\Local\Programs\Python\Python35-32\python.exe
"""

url=http://127.0.0.1:88/cgi-bin/tutor3.py
"""


import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')

html = """
<title>tutor3.py</title>
<h1>Greeting</h1>
<hr />
<p>%s</p>

<hr />"""

if not 'user' in form:
    print(html % 'Who are you?')
else:
    print(html % ('Hello, %s.' % form['user'].value))
