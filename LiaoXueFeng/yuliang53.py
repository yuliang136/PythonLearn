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