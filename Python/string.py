Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
>>> s1.upper()
'HELLO'
>>> s1.capitalize()
'Hello'
>>> si.casefold()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    si.casefold()
NameError: name 'si' is not defined. Did you mean: 's1'?
>>> s1.casefold()
'hello'
>>> s1.endswith('s')
False
>>> s1.count(h)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s1.count(h)
NameError: name 'h' is not defined
>>> s1.count('h')
1
>>> s1.find('e")
...         
SyntaxError: unterminated string literal (detected at line 1)
>>> s1.find('e')
...         
1
>>> s1.split(' ')
...         
['hello']
>>> s1.split('')
...         
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s1.split('')
ValueError: empty separator
>>> ValueError: empty separator
...         
SyntaxError: invalid syntax
