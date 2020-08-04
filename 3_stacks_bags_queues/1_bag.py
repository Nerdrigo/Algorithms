import sys

class Bag:
    """
    Creates a bag
    """

    class Node:
        """
        Creates a node as elem of stack
        """

        def __init__(self, item = None):

            self.item = item
            self.next = None

    def __init__(self):
        """
        Initializes bag object
        """
        self.size = 0
        self.first = None

    def __iter__(self):
        
        item = self.first
        yield item.item

        for idx in range(0,self.size - 1):
            item = item.next

            yield item.item

    def add(self, tiem):
        """
        Adds item to bag
        """

        #keeping track of what is to become second node
        old_first = self.first

        #creating new first
        self.first = Bag.Node(item)
        #set second node as first.next
        self.first.next = old_first

        #increase stack size
        self.size += 1

    def isEmpty(self):
        """
        Checks if stack is empty
        """

        return self.first == None

    def size(self):
        """
        Returns number of items in stack
        """

if __name__ == '__main__':

    collection = sys.argv[1:]

    print(collection)

    bag = Bag()
    
    for item in collection:
        bag.add(item)


    for marble in bag:
        print(marble)