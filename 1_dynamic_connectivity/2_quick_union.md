# Quick Union

The next algorithm is a method that conenctrates on speeding up the `union()` operation. It is based on the same data structure `id[]`, but we interpret the values differently. Specifically, the entry for each site is the name of another site in the same component (possibly itself), this connectoin is refered to as a *link*.

To implement `find()`, we start at a given site, follow the site's link to another site, until we reach a `root`, a site that has a link to itself. Two sites are connected iff they have the same root.

In the image below, one can se that when calling `find(5)`, we will go from `site 5 -> site 0 -> site 1`.
We also observe that `fin(4) = 8`, and `find(1) = 1`.

<img src="https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/images/1_quick_union_graph.jpg" width="600" height="300">

To implement `uninon(p,q)` we need to find the roots associated with `p` and `q`, then rename one of the components by linking one of these roots to the other. The choice is arbitrary.

The implementation can be found [here](https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/2_quick_union.py).

## Forest of trees representation.

The code for quick-union is compact, but a bit opaque. Representing the sites as nodes and links as arrows from one node to another gives a graphical representation of the data structure that makes it relatively easy to understand the operation of the algorithm (and hints at the importance of knowing descrete math for CS).

The resulting structures are trees, our `id[]` array is a parent-link representation of a forest (set) of trees, just as the ones shown in the image above.

## Analysis

Analyzing the cost of quick-union is a little bit more complicated than quick-find, because the cost is more dependent on the nater of the input.

In the best case `find()` just needs one array access to find the component of a site; in the worst case it needs `2N-1`(?) on account on its compare and assign operations. As illustrated below, the illustration assumes a component of 5 sites (labeled 0-4), where 4 is the root, and the sites are connected as follow: `0 -> 1 -> 2 ->3 ->4`.

<img src="https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/images/2_quick_union_analysis.jpg" width="600" height="600">

It is not difficult to construct a worst-case scenario for which the running time is quadratic. This follows from the proposition:

>**Proposition** The number of array accesses by `union()` and `connectected()` is the cost of two `find()` operaions (plus one `uinon()`)if the given sites are in different trees).
>
>**Proof** Immediate form the code.

>**Definition** The size of a tree is its number of nodes. The *depth* of a node ina tree is the number of links on the path from it to the root. The *height* of a tre i shte maximum depth among its nodes.

Supposing that we use quick-union for a problem that ends up with a single component, it means that we have to make at least `N-1` calls to `union()`.

If we input the pairs in order (`0 -> 1, 0 -> 2, 0 -> ...`); after `N-1` pairings This means, we will end up with a tree of height `N-1` with `0 -> 1 -> 2 -> ...`. By the proposition above, the array accesses for the `union()` operation for the pair `0 i` is `2i+1` (one linear `find()` operation plus one constant `find()` operation plus the union). Thus the total number of array accesses of the `find()` operations for these `N` pairs is `2(1+2+...+N) ~ <sup>2</sup>`.

### Clarification
(?) The book specifies `2N+1`, but given the diagrim shown and several times going through it I keep getting `2N-1`. I suppose there is a confusion with `N elements (5)` vs `N = 4`.
