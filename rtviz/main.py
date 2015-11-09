from time import time
from random import randrange 

from concurrent.futures import ThreadPoolExecutor
from functools import partial

from matplotlib import pyplot as plt


def func_timer(func, *params, verbose=False):
    """Takes in a function and some parameters to the function and returns the execution time"""
    start = time()
    func(*params)
    t = time() - start
    if verbose:
        print('function {func_name} took {time} seconds to complete given parameters'.format(
        func_name=func.__name__, time=t))
    return t


def list_generator(max_size, num_samples, n=10, upper_num=100):
    """Generates random integer lists with (sampled) lengths from range 1 to max_size.

    The difference between lengths (length spacing) of each list is delta, where delta is 
    defined as the floor division of max_size and num_samples.
    
    max_size: int
    The max length of a generated list

    num_samples: int
    The number of lists to generate

    returns:
    lst_of_rand_lsts: list of lists
    """


    def get_rand_list(n):
        """Returns a  list of random numbers."""
        return [randrange(upper_num) for x in range(n)] 

    assert max_size > num_samples
    delta = max_size // num_samples # uses the floor function to get difference between each sample.
    lst_lengths = [delta*x for x in range(1, num_samples + 1)] # Shift range by 1 to avoid making an empy list.
    #lst_of_rand_lsts = [get_rand_list(x) for x in lst_lengths]
    return (get_rand_list(x) for x in lst_lengths)

def runtime_generator(func, lists):
    """Maps func over each list in a list of lists and replaces each list element with the function runtime."""

    partial_func_timer = partial(func_timer, func)

    with ThreadPoolExecutor(max_workers=5) as executor:
        res = executor.map(partial_func_timer, lists)
        

    #res = [partial_func_timer(elem) for elem in lists]
    #assert 0 not in res# TODO: Make sure this isn't giving 0s
    return res

def runtime_lst_not_parallel(func, lists):
    """Maps func over each list in a list of lists and replaces each list element with the function runtime."""

    partial_func_timer = partial(func_timer, func)

    res = [partial_func_timer(elem) for elem in lists]
    #assert 0 not in res# TODO: Make sure this isn't giving 0s
    return res


def rtviz(func, *args, max_size=1000, num_samples=500, viz=True, verbose=True):
    """Takes in a function that receives an iterable as input.
    Returns a plot of the runtimes over iterables of random integers of increasing length.
    
    func: a function that acts on an iterable"""

    def subplot_generator(lst_lengths, func_times_lst):
            plt.plot(lst_lengths, func_times_lst, 'bo')
            plt.xlabel('length of random lists')
            plt.ylabel('function runtime (sec)')
            plt.title('Runtime of function {}'.format(func.__name__))
            return

    lst_of_lsts = list(list_generator(max_size, num_samples))
    lsts_len = [len(elem) for elem in lst_of_lsts]

    start = time()
    runtime_gen = runtime_generator(func, lst_of_lsts)
    t = time() - start
    
    if verbose == True:
        print('%s took %0.3fms.' % (func.__name__, t*1000.))


    subplot_generator(lsts_len, list(runtime_gen))
    if viz == True:
        plt.show()
    return

    


if __name__ == "__main__":

    rtviz(sorted)
