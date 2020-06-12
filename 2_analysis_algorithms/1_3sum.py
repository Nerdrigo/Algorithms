import sys
import time

class threeSum:
    def __init__(self, ints):
        '''
        Takes list of ints as input
        Outputs set of three integers that
        add up to 0
        '''

        #initializing 
        self.count = 0

        #count triples that sum to 0
        for i in range(len(ints)):
            for j in range(i+1,len(ints)):
                for k in range(j+1,len(ints)):
                    if ints[i] + ints[j] + ints[k] == 0:
                        self.count += 1

    def get_count(self):
        return self.count

if __name__ == '__main__':
    '''
    input is a txt file
    File is a list of ints
    For simplicity: assume input is always correct
    '''
    
    #Making sure input exist
    if sys.argv[1]:

        file = sys.argv[1]
        f = open(file, "r")

        #declaring int list
        ints = []

        #going through lines
        for line in f:
            #adding vals to list
            ints.append(int(line))

        #Start clock
        start = time.time()

        threeS = threeSum(ints)

        print(threeS.get_count())

        #Stop clokc
        end = time.time()
        total = end - start
        print("Time: " + str(total))

    else:
        print("Input file is needed")