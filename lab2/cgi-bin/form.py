#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import cgi
import html
import os
import http.cookies

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

count = cookie.get("count")

if count is None:
    print("Set-cookie: count=0 httponly")
else:
    print(f"Set-cookie: count={str(int(count.value) + 1)} httponly")

form = cgi.FieldStorage()
first_name = html.escape(form.getfirst("first-name", "empty"))
last_name = html.escape(form.getfirst("last-name", "empty"))
is_adult = form.getfirst("is-adult", "false")
state = form.getfirst("state", "male")

print("Content-type: text/html\n")

print("First name:", first_name)
print("<br>")
print("Last name:", last_name)
print("<br>")
print("Is adult:", "yes" if is_adult == "on" else "no")
print("<br>")
print("State:", state)
print("<br>")
print("Count of submit the form: " + str(count.value))
