Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
type(s1)
<class 'str'>
s2='hi'
type(s2)
<class 'str'>
id(s1)
2328076826112
id(s2)
140723620558264
s3=s1
id(s3)
2328076826112
s1='hi'
id(s1)
140723620558264
KeyboardInterrupt
list1=[10,20,30]
KeyboardInterrupt
st1[0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    st1[0]
NameError: name 'st1' is not defined. Did you mean: 's1'?
list1[1]
20
KeyboardInterrupt
list1[-1]
30
KeyboardInterrupt
st2=[100,'hi',100,69.34]
list2=[100,'hi',100,69.34]
list2[2]=43
list2
[100, 'hi', 43, 69.34]
KeyboardInterrupt
list2.append('xyz")
             
SyntaxError: unterminated string literal (detected at line 1)
list2.append('xyz')
             
KeyboardInterrupt
list2
             
[100, 'hi', 43, 69.34, 'xyz']
KeyboardInterrupt
list2.remove('xyz')
             
list2
             
[100, 'hi', 43, 69.34]
list2.append('xyz')
             
list2
             
[100, 'hi', 43, 69.34, 'xyz']
KeyboardInterrupt
list2.count(43)
             
1
KeyboardInterrupt
list2.insert(2,230)
             
list2
             
[100, 'hi', 230, 43, 69.34, 'xyz']
id(list1)
             
2328079921920
KeyboardInterrupt
list2.pop(200)
             
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list2.pop(200)
IndexError: pop index out of range
list2.pop(2)
             
230
list2
             
[100, 'hi', 43, 69.34, 'xyz']
KeyboardInterrupt
list1.clear()
             
list1
             
[]
del(list1)
             
list1
             
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list1
NameError: name 'list1' is not defined. Did you mean: 'list2'?
list1=list(list2)
             
list1
             
[100, 'hi', 43, 69.34, 'xyz']
KeyboardInterrupt
list1[3]=76
             
list1
             
[100, 'hi', 43, 76, 'xyz']
tuple1=(10,20,30,50)
             
tuple1
             
(10, 20, 30, 50)
tuple1[3]
             
50
uple1[3]=33
             
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    uple1[3]=33
NameError: name 'uple1' is not defined. Did you mean: 'tuple1'?
tuple1[3]=33
             
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    tuple1[3]=33
TypeError: 'tuple' object does not support item assignment
uple1[0:2:2]
             
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    uple1[0:2:2]
NameError: name 'uple1' is not defined. Did you mean: 'tuple1'?
tuple1[0:2:2]
             
(10,)
tuple1[0:4:2]
             
(10, 30)
tuple.index(30)
             
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    tuple.index(30)
TypeError: descriptor 'index' for 'tuple' objects doesn't apply to a 'int' object
tuple1.index(30)
             
2
tuple1.count(20)
             
1
list2.append(tuple1)
             
list2
             
[100, 'hi', 43, 69.34, 'xyz', (10, 20, 30, 50)]
KeyboardInterrupt
list2[3]
             
69.34
list2[5]
             
(10, 20, 30, 50)
list3=list(tuple1)
             
list3
             
[10, 20, 30, 50]
list3[2]
             
30
KeyboardInterrupt
list3[2:1]
             
[]
KeyboardInterrupt
list3[1:2]
             
[20]
KeyboardInterrupt
list2[5][3]
             
50
set1={10,20,30,40,50}
             
\
set1
             
{50, 20, 40, 10, 30}
set1[2]
             
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    set1[2]
TypeError: 'set' object is not subscriptable
set1.add(60)
             
set1
             
{50, 20, 40, 10, 60, 30}
set1.add('60')
             
set1.add(60)
             
set1
             
{50, 20, '60', 40, 10, 60, 30}
set1.add(60.0)
             
set1
             
{50, 20, '60', 40, 10, 60, 30}
>>> set2=set(set1)
...              
>>> set2
...              
{50, 20, '60', 40, 10, 60, 30}
>>> set2.remove('60')
...              
>>> set2
...              
{50, 20, 40, 10, 60, 30}
>>> set1
...              
{50, 20, '60', 40, 10, 60, 30}
>>> set1.union(set2)
...              
{40, 10, 50, 20, '60', 60, 30}
>>> set1.add(tuple1)
...              
>>> set1
...              
{(10, 20, 30, 50), 50, 20, '60', 40, 10, 60, 30}
>>> set1.add(list1)
...              
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    set1.add(list1)
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
>>> set1
...              
{(10, 20, 30, 50), 50, 20, '60', 40, 10, 60, 30}
