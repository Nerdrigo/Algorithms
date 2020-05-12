# Quick-find

This approach is to maintain the invariant that `p` and `q` are connected iff `id[p] == id[q]`. In other words all sites in the same component **must have the same value in `id[]`**.

This method is called "quick-find" because `find(p)` just returns `id[p]`.

To combine two components (`p` and  `q`), we have to make all of the `id[]` entries corresponding to both sets of sites the same value. To do so we got through the array changing all the entries with values equal to `id[p]` to the value `id[q]`. The code implementation for *quick-find* can be found [here]() 
