# Weighted Quick Union

An improvement to the quick uinon algorithm would be: rather than arbitrarily connecting one one tree to another, we keep track of the sieze of each tree, and always connect the smaller to the larger. 

The implementation requires slightly more code and another array that will hold the node counts of each tree. The implementation can be found [here](https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/3_weighed_quick_union.py).

## Analysis

The worst case scenario for wighted quick union is when the size of the trees to be merged are always equal (and a power of two). These trees have a property that the height of a tree of 2<sup>n</sup> nodes is at most `n`(?).

Merging two tres of 2<sup>n</sup> nodes will result in a tree of 2<sup>n+1</sup> nodes, and the height will be `n+1`. This observation generalizes to provide a proof that the weighted algorithm can guarantee *logarithmic* performance.

>**Proposition** The depth of any node in a forest built by weighted quick-union for `N` sites is at most `lg N`.
>
>**Proof** We prove a stronger fact by induction: The heigh of every tree of size `k` in the forest is at most `lg k`. The base case follows from the fact that the tree height is `0` when `k` is `1`. By inductive hypothesis, assume that the tree height of a tree of size `i` is at most `lg i` for all `i < k`. When we combine a tree of size `i` with a tree of size `j` with `i <= j` and `i + j = k`, we increase the depth of each node in the smaller set by 1, but they are now a tree of size `i + j = k`, so the property is preserved because `1 + lg i = lg 2 + lg i = lg (2*i) = lg(i+i) <= lg(i+j) = lg k`.

>**Crollary** For weighted quick union with `N` sites, the worst-case *order of growth* of the cost of `find()`, `connected()` and `union()` is `lg N`.
>
>**Proof** Given that the depth of a tree of size `N` is at `lg N`, the *order* of growth of `find()` is `lg N`. The implementation of `union()` and `connected()` is just twice the cost of `find()`, so they are also of the *order* of `lg N`.

The implications of the proposition and it's corollary is that weighted quick uninon is the only one of the three algorithms that can feasible be used for huge practical problems.

### Clarificaiton
`lg` is log base 2.

(?) Looking at the figure below, which is an example of a worst case scneario, we can see that when the tree is of size 8 (2<sup>3</sup>), it's height is 3. To prove the property we can use induction.

<img src="https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/images/3_weighted_worst_case.png">

The figure is a wost case scenario, as it is imposible (by the way the algorith works) to create a one sided long chain. If you want to create long chains, you have to create them the way the figure illustrates.
