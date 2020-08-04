import sys

class Queue():
    """
    Creates a queue
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
        Initializes bag queue
        """

        self.size = 0
        self.first = None
        self.last = None

    def __len__(self):
        return self.size

    def enqueue(self, item):
        """
        Adds item to queue
        """

        #getting ref to previous last
        old_last = self.last

        #creating new last
        self.last = Queue.Node(item)

        if self.isEmpty():
            self.first = self.last
        else:
            #set reference from next-2-last -> last
            old_last.next = self.last

        #increase size of queue
        self.size +=1

    def dequeue(self):
        """
        Removes item from queue
        """

        #getting first node item
        item = self.first.item
        
        #setting second node as new first
        self.first = self.first.next

        #if it's now empty set last as None
        if self.isEmpty():
            self.last = None

        #decrease queue size
        self.size -= 1

        return item

    def isEmpty(self):
        """
        Checks if stack is empty
        """

        return self.first == None

    def size(self):
        """
        Returns number of items in stack
        """

        return self.size


if __name__ == '__main__':

    collection = sys.argv[1:]

    queue = Queue()
    output = []
    
    for item in collection:
        if item != "-":
            queue.enqueue(item)
        else:
            output.append(queue.dequeue())

    print(output)