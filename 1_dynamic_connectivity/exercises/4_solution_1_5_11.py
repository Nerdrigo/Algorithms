import sys

#this implementation differs on the original
#diff, this keeps count of times id[] is accessed

class weighted_quick_union_UF:
    def __init__(self, N):
        '''
        Set count to N
        Initialize component id array
        '''
        self.count = N
        self.id = [i for i in range (N)]
        self.sz = [1] * N
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
        #if p != id[p] it is not a root
        while p != self.id[p]:
            self.access += 2 #while and assignment
            p = self.id[p]

        #the one time we didn't access loop
        self.access += 1

        return p

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
        root_p = self.find(p)
        root_q = self.find(q)

        #if roots are not the same connect them
        if root_p != root_q:
            if self.sz[p] < self.sz[q]:
                #since p is smaller, p gets added to q
                for i in range(len(self.id)):
                    self.access += 1
                    #if root of site i is p, change to component q
                    if self.find(self.id[i]) == root_p:
                        self.access += 1
                        self.id[i] = root_q
                #size of q increases by p
                self.sz[root_q] += self.sz[root_p]
            else:
                for i in range(len(self.id)):
                    self.access += 1
                    #if root of site i is q, change to component p
                    if self.find(self.id[i]) == root_q:
                        self.access += 1
                        self.id[i] = root_p
                self.sz[root_p] += self.sz[root_q]


            #reducing component count
            self.count -= 1
            
            print(str(p) + " " + str(q))
            print(self.id)
            print(self.sz)
            print("\n")

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
        uf = weighted_quick_union_UF(int(num_site))

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