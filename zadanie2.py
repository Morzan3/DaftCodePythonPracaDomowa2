from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def deprecated_2(function):

    def wrapper(*args, **kwargs):
        eprint("Funkcja {} jest przestarzała i zostanie usunięta w następnej wersji".format(function.__name__))
        function(*args, **kwargs)
    return wrapper

@deprecated_2
def dluga_nazwa_do_testow():
  print("test")


dluga_nazwa_do_testow()
dluga_nazwa_do_testow()
