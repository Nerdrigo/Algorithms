# Quick Union

The next algorithm is a method that conenctrates on speeding up the `union()` operation. It is based on the same data structure `id[]`, but we interpret the values differently. Specifically, the entry for each site is the name of another site in the same component (possibly itself), this connectoin is refered to as a *link*.

To implement `find()`, we start at a given site, follow the site's link to another site, until we reach a `root`, a site that has a link to itself. 

In the image below, one can se that when calling `find(5)`, we will go from `site 5 -> site 0 -> site 1`.
We also observe that `fin(4) = 8`, and `find(1) = 1`.

<img src="https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/images/1_quick_union_graph.jpg" width="600" height="300">
