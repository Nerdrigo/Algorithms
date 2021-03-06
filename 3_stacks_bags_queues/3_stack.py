import sys

class Stack:
    """
    Creates a stack
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
        Initializes bag stack
        """

        self.size = 0
        self.first = None

    def push(self, item):
        """
        Adds item to stack
        """

        #keeping track of what is to become second node
        old_first = self.first

        #creating new first
        self.first = Stack.Node(item)
        #set second node as first.next
        self.first.next = old_first

        #increase stack size
        self.size += 1


    def pop(self):
        """
        Removes item from stack
        """
        #getting first node item
        item = self.first.item

        #setting second node as first
        self.first = self.first.next

        #reduce stack size
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

    print(collection)

    stack = Stack()
    output = []
    
    for item in collection:
        if item != "-":
            stack.push(item)
        else:
            output.append(stack.pop())

    print(output)
    