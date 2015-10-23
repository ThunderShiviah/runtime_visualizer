
from matplotlib import pyplot as plt



def sort_compare(max_size, num_samples, func):
    """Returns two lists corresponding to the lengths of random lists and the runtime
       execution of function func on those lists.
       """
    assert max_size > num_samples
    delta = max_size // num_samples # uses the floor function to get difference between each sample.
    lst_lengths = [delta*x for x in range(num_samples)] 
    lst_of_rand_lsts = [get_rand_list(x) for x in lst_lengths]
    func_times_lst = [func_timer(func, 50, lst) for lst in lst_of_rand_lsts]
    
    return lst_lengths, func_times_lst

def set_compare(max_size, num_samples, func):
    """Returns two lists corresponding to the lengths of random lists and the runtime
       execution of function func on those lists.
       """
    assert max_size > num_samples
    delta = max_size // num_samples # uses the floor function to get difference between each sample.
    lst_lengths = [delta*x for x in range(num_samples)] 
    lst_of_rand_lsts = [get_rand_list(x) for x in lst_lengths]
    func_times_lst = [func_timer(func, lst) for lst in lst_of_rand_lsts]
    
    return lst_lengths, func_times_lst
    
    
def subplot_generator(lst_lengths, func_times_lst):
    plt.plot(lst_lengths, func_times_lst, 'bo')
    return
    

def sort_plotter(max_size, num_samples, *funcs):
    """Plots functions vs execution time.
    
    Details
    -------
    Creates plots of each function in *funcs wrt 
    execution time by sampling num_samples lists of incremental
    length up to length max_size.
    
    Parameters
    ----------
    max_size: int
        The length of the final list sampled.
    num_samples: int
        The number of times to sample_the function.
    *functs: iterator
        An iterator containing the functions we wish to sample.
    
    Returns
    -------
    plots: matplotlib.pyplot
        Returns subplots with the length of the sampled 
    list as the x-axis, and the average runtime of the 
    function over the list using timeit.
    NOTE: timeit defaults to 1000 function calls.
        
    """
 
    print(type(funcs))
    # sort_compare(max_size, num_samples, func)

    return

if __name__ == "__main__":
    lst_lengths, func_times_lst = sort_compare(10000, 1000, brute_force_search)
    subplot_generator(lst_lengths, func_times_lst)
