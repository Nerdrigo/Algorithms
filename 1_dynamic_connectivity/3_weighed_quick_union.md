# Weighted Quick Union

An improvement to the quick uinon algorithm would be: rather than arbitrarily connecting one one tree to another, we keep track of the sieze of each tree, and always connect the smaller to the larger. 

The implementation requires slightly more code and another array that will hold the node counts of each tree. The implementation can be found here.