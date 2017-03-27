import time


def my_timeit(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        end = time.time()
        print("Czas wykonania {}: {} ms".format(function.__name__, (end - start)*1000))
    return wrapper

@my_timeit
def dluga_nazwa_do_testow():
  print("test")


dluga_nazwa_do_testow()
dluga_nazwa_do_testow()
