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
    
    #reading input file
    file = 'tinyUF.txt'
    f = open(file, "r")

    #going through lines
    for line in f:
        #spliting values
        values = line.split(" ")

        #if reading first line instantiate
        if len(values) ==1:        
            uf = UF(int(values[0]))

        else:
            print(str(int(values[0])) + "   " + str(int(values[-1])))