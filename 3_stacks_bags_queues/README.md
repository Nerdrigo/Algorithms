# Bags, Queues, and Stacks

Several fundamental data types invovle collections of objects, and the operations revolving around adding, removing, or examining objects in the collection. For this we consider the bag, the stack, and the queue.

## APIs

We begin by defining the APIs bags, stacks and queues.

Each contains a no-argument constructor, a method to add an item to the collection, a method to test whether the collection is empty, and a method that returns the size of the collection. Stack and Queue each have a method to remove a particular item from the collection.

>In the book, the APIs implement the *Iterable* class(?), seems to be either not needed in python, or it needs the use of *sequence*. Will update in future.

The implementations are found:
* [Bag](https://github.com/Nerdrigo/algorithms/blob/master/3_stacks_bags_queues/1_bag.py)
* [Queue](https://github.com/Nerdrigo/algorithms/blob/master/3_stacks_bags_queues/2_queue.py)
* [Stack](https://github.com/Nerdrigo/algorithms/blob/master/3_stacks_bags_queues/3_stack.py)

### Bags

A bag is a collection of objects where removing items is not supported, its purpose is to provide a way to collect and iterate through items. The order of the iteration is unspecified. This is akin to having a bag of marbles, the order of the marbles is inconsequential, but you can always examine one by one.

### FIFO queues

A FIFO queue is a collection based on the *first-in-first-out* policy. Which is the policy followed by reqular lines of people waiting in the supermarket or the bank.

A typical reason to use a queue in an application is to save items in a collection while at the same time preserving their relative order.

### Pushdown stacks

A pushdown stack is a collection based on the *last-in-first-out* principle. It is akin to stacking letters (or mails) on a table, and opening the one on top (the one that was placed last).

A typical reason to use a stak in an aplication is to save items in a collection while at the same time reversing their relative order.


### Notes

The book goes on explaining things relating primarily to Java code, facts, limitations, etc. The first iteration of the aformentioned data structures had some limitations that would be addressed in the next section.

## Linked lists

>**Definition** A *linked list* is a recursvie data structure that is either empty (null) or a reference to a node having a generic item and a reference to a linked list.

The node is an abstract entity that might hold any kind of data, in addition to the node reference that characterizes its role in building linked lists.

### Node record

A node has two instance varibles: an Item and a Node. We define Node within the class we want to use it

The implementation of `Node` is as follows:

```
class Node:

    def __init__(self, item = None):

        self.item = item
        self.next = None
```

### Building a linked list

Now, from the recursive definition, we can represent a linked list with a variable of type Node simply by ensuring that its value is either null or a ref- erence to a Node whose next field is a reference to a linked list. See page 143 of the book to see example.

When tracing code that uses linked lists and other linked structures it is useful to have a visual representation where
* We draw a rectangle to represent each object
* We put the values instance variables within each rectangle
* We use arrows that point to the refeenced objects to depict references.

### Inserting from the beggining

To insert a new node to a linked list at the beginning is very simple. For example, to insert the string `a` at the beginning of a linked list with first node `first`, we assign `old_first = first` and assign first to a new node with `item = "a"` and `next = old_first`.

### Remove from the beginning

To remove from the beginning, the only thing you have to do is re-assing first like `first = first.next`.

### Insert at the end

The method to insert a node at the end is similar to add a node at the beginning, you need to keep reference of your last node (`last`) and create a `old_last` copy. However, complications arise for the node at the end because every method that modifies the list needs code to check whether that variable needs to be modified. 

The code in the previous section would not work, since removing the first node in the list might in- volve changing the reference to the last node in the list, since when there is only one node in the list, it is both the first one and the last one.

### Insert/remove at other positions

In order to accomplish this it is necessary to traverse the entire list. Such a solution is undesirable because it takes time proportional to the length of the list. The standard solution to enable arbitrary insertions and deletions is to use a doubly-linked list, where each node has two links, one in each direction. 

### Traversal

To traverse the linked list we can use the following code
```
x = first

while x != None:
    
    #Process x.item
    
    x = x.next
```