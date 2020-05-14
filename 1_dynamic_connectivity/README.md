This is the first lesson in the algorithms Coursera course.
I'm following the MOOC structure, but mainly use the book as a guide, rather than the videos.

# Dynamic connectivity

## Problem Specification

The input is a pair of integers `p` and `q`.

Each integer represents an object, it is a label, e.g:
* person 1
* computer 3
* DB 7
* Yavin 4

We interpret the pair `p q` as "p is connected to q" (`p -> q`). We assume "is connected to" is an equivalent relation, which means that is:
* Reflexive: `p` is connected to `p`.
* Symmetric: if `p -> q`, then `q -> p`.
* Transitive: if `p -> q` and `q -> r`, then `p -> r`. 

The objective is to create a program that will determine if `p` and `q` are in the same  equivalence class. Two objects are in the same equivalence class iff they are connected. We can think of an equivalence class as a set of related objects.

The challenge is to create a data structure that will allow us to efficiently determine if `p` and `q` are connected or not. This is the dynamic connectivity problem. It has applications in:
* Networks
* Variable name equivalence (if two variables refer to the same obj)
* Mathematical sets

The first task is to specify a problem in a precise manner. We often modify the problem specification after finding that it is more difficult or expensive than originally expected. Sometimes we might change the problem specification after finding that the algorithm provides more usefull information than originally expected.

To specify the problem we develop an API that encapsulates the basic operations that we need:
* Initialize
* Add a connection between sites (sites = numbers).
* Identify a component containing a site (component = equivalence class).
* Determine if two sites share the same component.
* Count the number of components.

The API will be as follows:
```
class UF
    UF(int N)
    void union(int p, int q)
    boolean connected(int p, int q)
    int count()
```

* `union()` merges two components (connects two sites)
* `find()` returns integer component identifier for a given site (?).
* `count()` returns number of components, `count()` starts as N when `UF(N)` is initialized (??), and decreases by one each time `union()` succesfully connects two sites.

**KEY IDEA:** the development of an algorithmic solution to our problem is reduced to developing an implementaion of the API. Every implementation has to:
* Define a data structure to represent known connections.
* Develop efficient method implementations based on that data structure.

The nature of the data structure has a direct impact on the effiency of the algorithms. Data structure and algorithm design go hand in hand.   

### Explanations
(?) `site 1` can be found in `component 1` or `component 2`. The *integer component identifier* of `component 1` is `1`. If `site 1` is in `component 1`, then `find(1) = 1`, if `site 1` is in `component 2` then `find(1) = 2`.

(??) We start with N components becasuse when we initialize `UF(N)`, we have `N` unconnected sites, each site is it's own component.

## Overall `UF` remarks

The design of the API specifies that sites and connections will be represented by `int` values between `0` and `N-1`, so it makes sense to use a *site-indexed array* `id[]` as our basic data structure to represent components. 

This means that for the component for `site i` will be given by `id[i]`. In the begining, when no connections are made `id[i] = i`, as every site is it's own component. When joining sites `p` and `q` then `id[p] = id[q]`, because `id[p]` is the component of `p`, and `id[q]` is the component of `q`, when `p -> q` the component(*equivalence class*) is the same, hence `id[p] = id[q]`.

Given the explanation above, it follows that `find(i)` will return `id[i]`. The implemenation of `connected(p, q)` will be a one-liner: `return find(p) == find(q)`.

In summary, our starting point is [Algorithm UF](https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/basic_UF.py). The algorithm maintains two instance variables, the count of components and the array `id[]`. Implementations of `find()` and `union()` are the topic of the lesson.

The API is tested with the files that come in the [book's website](https://algs4.cs.princeton.edu/15uf/).

To analyze the efficiency of the algorithms, we focus the number of times each article access an array entry (for read or write). This is due to the fact that the running time of the algorithm on a particular machine is proportional to this quantity. If one algorithm access an array entry one time for each pair, versus another one that does it 10 times for each pair, it is obvious that the first algorithm is faster.

We shall consider three different implementations, all based on using the site-indexed id[] array, to determine whether two sites are in the same con- nected component.
* [Quick find](https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/quick_find.md)
* [Quick union](https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/2_quick_union.md)
* [Weighted quick union](https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/3_weighed_quick_union.md)

## Optimal Algorithms

In order to near constant time operation performance a method known as path compression can be used. Ideally, we would want to link every node directly to it's root, but we don't want to pay the price of moving a large number of links (like quick find). We can approach the ideal simply by making all nodes we *examine* link to the root. To implement path compression, we just add another loop to `find()` that sets the `id[]` entry corresponding to each node encountered along the way to link directl to the root. The net result is an almost flat tree. The method is simple an effective, but its effect is not discernible from weighted quick union in practical situations. *Weighted quick union with path compression is optimal but not quite constant-time per operation*. No program can guarantee constant time per operation. Weighted quick-union with path compression is very close to the best that we can do for this problem.

## Perspective

Each of the UF implementations we considered is an improvement over the prvious in some intuitive sense, but the process was smooth because we have the benefit of hindsight. 

The implrementations are simple and the problem is well specified, so we can evaluate our algorithms directly by running empirical studies. We can also use these studies to validate mathematical results that quantify the performance of these algorithms.

When possible, we follow the basic steps for fundamental problems:
* Decide on a complete and specific problem statement, including identifying fundamental abstract op that are intrinsic to the problem and an API.
* Carefully develop a succinct implementation for a straightforward algorithm, using well thought out development client and realistic input data.
* Know when an implementation could not possibly be used to sovle problems on the scale contemplated and must be improved or abandoned.
* Develop improved implementations through the process of stepwise refinement, validating the efficacy of ideas for improvement through empirical analysis, matehmatical analysis, or both.
* Find high-level abstract representation of data structures or algorithms in operation that enable effective high-level design of improved versions.
* Strive for worst-case performance guarantees when possible, but accept good performance on typical data when available.
* Know when to leave further implementations for detailed in-depth study to skilled researchers and move on to the next problem.
