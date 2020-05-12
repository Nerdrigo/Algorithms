# Quick-find

## Implementation

This approach is to maintain the invariant that `p` and `q` are connected iff `id[p] == id[q]`. In other words all sites in the same component **must have the same value in `id[]`**.

This method is called "quick-find" because `find(p)` just returns `id[p]`.

To combine two components (`p` and  `q`), we have to make all of the `id[]` entries corresponding to both sets of sites the same value. To do so we got through the array changing all the entries with values equal to `id[p]` to the value `id[q]`. The code implementation for quick-find can be found [here](https://github.com/Nerdrigo/algorithms/blob/master/1_dynamic_connectivity/1_quick_find_UF.py).

## Analysis

The `find()` operation is quick, the algorithm only acces the `id[]` array once. But it is not useful for larger problems, because `union()` needs to scan all the array for each connection.

>**Proposition** The quick-find algorithm uses one array access for each call to `find()` and between`N+3` and `2N+1` array accesses for each call to `union()`
>
>**Proof**:
>It is immediate from the implementation that `find()` onle accesses `id[]` once (in the `return` statement).
>
>For `union()`, we start by accessing `id[]` 2 times, we have to read `id[p]` and `id[q]`.
>
>If a connection has not yet made, we have to read the array `N` times, if only one site needs to change component, then we access the array one more, for a total of `2 + N + 1 = N+3`. 
>
>If we have to move `N-1` sites to another component, then we access the array a total of `2 + N + (N-1) = 2N+1`.

Supposing that we use quick-find for a problem that ends up with a single component, it means that we have to make at least `N-1` calls to `union()`. This means, we will end up accessing `id` at least `(N+3)(N-1) ~ N<sup>2</sup>` array accesses, leading to the fact that dynamic connectivity with quick-find can be a *quadratic-time* process.