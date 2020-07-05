import sys
import time

#Define inputs/starting input        

def time_trial(inputs):
    #Start clock
    start = time.time()

    #Do test
    #test_func(inputs)

    #Stop clokc
    end = time.time()
        
    total = end - start
        
    return total        

#Perform double test
## prev = time_trial(starting_input)

##for input in inputs:
####    time = time_trial(input)
####    print(input + time + time/prev)
####    prev = time

## while True
####    time = time_trial(2*input)
####    print(input + time + time/prev)
####    prev = time