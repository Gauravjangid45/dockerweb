#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess
import cgi

form = cgi.FieldStorage()
uinput=form.getvalue("cmd")
out1=subprocess.getoutput("sudo "+uinput)
print(out1)
