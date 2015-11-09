
from rtviz.main import *

def func_timer_test():
    assert func_timer(max, [i for i in range(1000)]) != 0
    assert type(func_timer(max, [i for i in range(1000)])) == type(0.1)

def list_generator_test():

    assert len(list(list_generator(10,5))) == 5
    assert list(list_generator(2,1)) != [[]]
    assert type(next(list_generator(2,1))) == type([])

def runtime_lst_test():

    def f(n): return n**2
    assert len(list(runtime_generator(f, [i for i in range(10)]))) == 10


