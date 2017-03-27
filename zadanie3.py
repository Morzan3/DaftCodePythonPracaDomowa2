from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def deprecated_3(function):
    if not hasattr(deprecated_3, 'calls'):
        deprecated_3.calls = dict()

    def wrapper(*args, **kwargs):
        deprecated_3.calls[function.__name__] += 1
        eprint("Funkcja {} jest przestarzała i zostanie usunięta w następnej wersj. Numer wywołania: {}".format(function.__name__, deprecated_3.calls[function.__name__]))
        function(*args, **kwargs)
    deprecated_3.calls[function.__name__] = 0
    return wrapper

@deprecated_3
def dluga_nazwa_do_testow():
  print("dluga")

@deprecated_3
def krotka_nazwa():
  print("krotka")

dluga_nazwa_do_testow()
dluga_nazwa_do_testow()
dluga_nazwa_do_testow()
krotka_nazwa()
krotka_nazwa()

print(deprecated_3.calls['dluga_nazwa_do_testow'])
print(deprecated_3.calls['krotka_nazwa'])
