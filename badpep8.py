import sys
import random


# multiple imports
def foo_bar(arg1, arg2, arg3, arg4):
	return arg1, arg2, arg3, arg4


def bar(*args):
	return 2 + 2


# Bad class name, bad spacing, bad indentation
class treehouse:
	def one(self):
		return 1
	
	def two(self):
		return 2


# bad indentation and whitespace
alpha, beta, charlie, delta = fooBar(
	"a long string", 
	"a longer string", 
	"yet another long string", 
	"and other crazy string"
	)


# bad spacing
one = 1
three = 3
fourteen = 14 # make fourteen equal to 12

print(alpha)
print(fourteen)

print(treehouse().two())