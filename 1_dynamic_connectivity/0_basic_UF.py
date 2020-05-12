import sys

class UF:
    def __init__(self, N):
        '''
        Set count to N
        Initialize component id array
        '''
        self.count = N
        self.id = [i for i in range (N)]
        print("starting UF with " + str(N) + " sites")

    def get_count(self):
        '''
        returns number of components
        '''
        return self.count

    def find(self, p):
        '''
        returns component of site p
        '''
        #some code

    def connected(self, p, q):
        '''
        returns true if p->q
        returns false otherwise
        '''
        return self.find(p) == self.find(q)

    def union(self, p, q):
        '''
        if p->q, it does nothing
        else it connects p to q.
        '''
        #some code

if __name__ == '__main__':
    '''
    input is a txt file
    first line has number of sites
    following lines pairs of num to be connnected
    ex:
    3
    1 2
    3 1
    For simplicity: assume input is always correct
    '''
    
    #Making sure input exist
    if sys.argv[1]:

        file = sys.argv[1]
        f = open(file, "r")

        #reading first line
        num_site = next(f)

        #going through lines
        for line in f:
            #spliting values
            values = line.split(" ")
            #printing values
            print(str(int(values[0])) + "   " + str(int(values[-1])))

    else:
        print("Input file is needed")