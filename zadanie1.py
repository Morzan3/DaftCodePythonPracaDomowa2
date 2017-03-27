from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def deprecated_1(function):
  eprint("Funkcja {} jest przestarzała".format(function.__name__))
  return function

@deprecated_1
def test():
  print(test)
