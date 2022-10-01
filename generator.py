# Generator for infinite sequence
def infinite_sequence():
    '''
    for the function test
    import generator
    gen = generator.infinite_sequence()
    next(gen)
    >>0
    next(gen)
    >>1
    and so on..
    '''
    num = 0
    while True:
        yield num
        num+=1



#Generator for finit sequence
def finite_sequence():
    '''
    when you replace return with yield it is converted to generator

    '''
    lc = [1, 2, 3, 4, 5]
    for num in lc:
        yield num

# Similar to list comprehension but with round bracket
'''
sq_lc1 = [i**2 for i in range(10000)] 
sq_lc2 = (i**2 for i in range(10000)) # this is generator

#To check the memory size
import sys
sys.getsizeof(sq_lc1)
sys.getsizeof(sq_lc2)

#To check speed
import cprofile
cProfile.run('sum((i**2 for i in range(10000)))') # this one is slower but memory efficientexit
cProfile.runn('sum([i**2 for i in range(10000)])')

'''
#Creating a datapipeline using generator
file_name = 'test.csv'
lines = (line for line in open('/test_data/'+file_name))
list_line = (s.rstrip().split(',') for s in lines)
cols = next(list_line)
my_dict = (dict(zip(cols, data) for data in list_line))
funding = (
    int(cy_dict["raisedAmt"])
    for cy_dict in my_dict
    if cy_dict["round"] == 'a'
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")