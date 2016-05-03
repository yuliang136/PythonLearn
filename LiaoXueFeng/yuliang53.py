# -*- coding: utf-8 -*-

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

def person(name,age,**kw):
	print 'name:',name, 'age:',age, 'other:',kw

def func(a,b,c=0,*args,**kw):
	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)


'''
L = []
n = 1
while n <= 99:
	L.append(n)
	n = n + 2
print L
'''

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

'''
r = []
n = 3
for i in xrange(0,n):
	r.append(L[i])

print r
'''


'''
print L[-2:-1]
'''

'''
L = range(100)
print L[-10:]
'''


d = {'a':1, 'b':2, 'c':3}

'''
for key in d:
	print key
'''

'''
for value in d.itervalues():
	print value
'''

'''
for k, v in d.iteritems():
	print 'k= ', k, 'v= ',v
'''

'''
for ch in 'ABC':
	print ch
'''

'''
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123,Iterable)
'''

'''
for i,value in enumerate(['A','B','C']):
	print i, value
'''

'''
for x,y in [(1,1 ), (2, 4), (3, 9)]:
	print x, y
'''

'''
d = {'x':'A', 'y':'B', 'z':'C'}
for k,v in d.iteritems():
	print k, '=', v
'''

'''
d = {'x':'A', 'y':'B', 'z':'C'}
show = [k + '=' + v for k,v in d.iteritems()]

print show
'''

L = ['Hello', 'World', 18, 'Apple', None]
show = [s.lower() for s in L if isinstance(s, str)]
print show























