import random

def stack_arrray(*args):
    print(str(args)+ " ")
def heap_array(*args):
    loc = random.randint(1,8)
    for i in range(1,loc): print("-- ")
    print(str(args))
    for i in range(loc, 8): print("--" )
    

stack_arrray(2,3,4,5)
heap_array(2,3,4,5)
