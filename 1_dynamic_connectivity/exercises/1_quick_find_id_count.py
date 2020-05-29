import sys

#this implementation differs on the original
#diff, this keeps count of times id[] is accessed

class quick_find_UF:
    def __init__(self, N):
        '''
        Set count to N
        Initialize component id array
        '''
        self.count = N
        self.id = [i for i in range (N)]
        print("starting UF with " + str(N) + " sites")

        #num array acchess counter
        self.access = 0

    def get_count(self):
        '''
        returns number of components
        '''
        return self.count

    def get_id_access(self):
        '''
        returns number of components
        '''
        return self.access

    def find(self, p):
        '''
        returns component of site p
        '''
        self.access += 1
        return self.id[p]

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

        #Getting compontnets for p and q
        p_val = self.find(p)
        q_val = self.find(q)

        #if not connected, connect p with q
        if not p_val == q_val:
            
            for i in range(len(self.id)):
                #looking for sites in component p
                self.access += 1 #for if statement
                if self.id[i] == p_val:
                    #moving sties to component q
                    self.access += 1 #for assignment
                    self.id[i] = q_val
            print(str(p) + " " + str(q))

            #decreasing component count
            self.count -= 1

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

        #instantiation obj
        uf = quick_find_UF(int(num_site))

        #going through lines
        for line in f:
            #spliting values
            values = line.split(" ")
            #connecting values
            uf.union(int(values[0]), int(values[-1]))

        print(str(uf.get_count()) + " components")
        print("Number of array access: " + str(uf.get_id_access()))
        print(uf.id)
    else:
        print("Input file is needed")