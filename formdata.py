#!C:\Users\triosStudent\AppData\Local\Programs\Python\Python35-32\python.exe

import cgi
form = cgi.FieldStorage()
print('Content-type: text/html')

html = """
<title>formdata.py</title>
"""

print(html)
      
for key in form:
    print(key+' : '+form[key].value)
    print('<br />')
