This is the frist lesson in the algorithms Coursera course.
I'm following the MOOC structure, but mainly use the book as a guide, rathern than the videos.

# Dynamic connectivity

## Problem Specification

The input is a pair of integers `p` and `q`.

Each integer represent an object, it is a label, e.g:
* person 1
* computer 3
* DB 7
* Yavin 4

We interpret the pair `p q` as "p is connected to q" (`p -> q`). We assume "is connected to" is an equivalent relation, which means that is:
* Reflexive: `p` is connected to `p`.
* Symmetric: if `p -> q`, then `q -> p`.
* Transitive: if `p -> q` and `q -> r`, then `p -> r`. 

The objective is to create a program that will determine if `p` and `q` are in the same  equivalence class. Two objects are in the same equivalence class iff they are connected. We can think of an equivalence class as a set of related objects.

The challenge is to create a data structure that will allow us to efficiently determine if `p` and `q` are connected or not. This is the dynamic connectivity problem. I has applications in:
* Networks
* Variable name equivalence (if two variables refer to the same obj)
* Mathematical sets

The first task is to specify a problem in a precise manner. We often modify the problem specification in finding that it is more difficult or expensive than originally expecte. Sometimes we might change the problem specificain after finding that the algorithm provides more usefull information than originally expected.

To specify the problem we develop an API that encapsulates the basic operations that we need:
* Initialize
* Add a connection between sites (sites = numbers).
* Identify a component containing a site (component = equivalence class).
* Determine if two sites share the same component.
* Count the number of components.