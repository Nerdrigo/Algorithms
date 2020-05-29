## Exercises

**1.5.1** Contents of `id[]` and number of times array is accessed for each input using quick-find:
* Number of array access: 110
* id = [1, 1, 1, 1, 1, 1, 6, 1, 1, 1]


**1.5.2** Contents of `id[]` and number of times array is accessed for each input using quick-union:
* Number of array access: 36
* id = [9, 1, 1, 4, 1, 8, 6, 2, 1, 4]


**1.5.3** Contents of `id[]` and number of times array is accessed for each input using quick-union:
* Number of array access: 32
* id = [0, 7, 7, 0, 3, 7, 6, 0, 5, 0]


**1.5.4** Contesnts of `id[]` and `sz[]` and # of array accesses for each input corresponding to weighted QU examples in text.
* Reference
```
4 3
id = [0, 1, 2, 4, 4, 5, 6, 7, 8, 9]
sz = [1, 1, 1, 1, 2, 1, 1, 1, 1, 1]

3 8
id = [0, 1, 2, 4, 4, 5, 6, 7, 4, 9]
sz = [1, 1, 1, 1, 3, 1, 1, 1, 1, 1]

6 5
id = [0, 1, 2, 4, 4, 6, 6, 7, 4, 9]
sz = [1, 1, 1, 1, 3, 1, 2, 1, 1, 1]

9 4
id = [0, 1, 2, 4, 4, 6, 6, 7, 4, 4]
sz = [1, 1, 1, 1, 4, 1, 2, 1, 1, 1]

2 1
id = [0, 2, 2, 4, 4, 6, 6, 7, 4, 4]
sz = [1, 1, 2, 1, 4, 1, 2, 1, 1, 1]

5 0
id = [6, 2, 2, 4, 4, 6, 6, 7, 4, 4]
sz = [1, 1, 2, 1, 4, 1, 3, 1, 1, 1]

7 2
id = [6, 2, 2, 4, 4, 6, 6, 2, 4, 4]
sz = [1, 1, 3, 1, 4, 1, 3, 1, 1, 1]

6 1
id = [6, 2, 6, 4, 4, 6, 6, 2, 4, 4]
sz = [1, 1, 3, 1, 4, 1, 6, 1, 1, 1]

Number of array access: 50
```
* Worst case
```
0 1
id = [0, 0, 2, 3, 4, 5, 6, 7]
sz = [2, 1, 1, 1, 1, 1, 1, 1]

2 3
id = [0, 0, 2, 2, 4, 5, 6, 7]
sz = [2, 1, 2, 1, 1, 1, 1, 1]

4 5
id = [0, 0, 2, 2, 4, 4, 6, 7]
sz = [2, 1, 2, 1, 2, 1, 1, 1]

6 7
id = [0, 0, 2, 2, 4, 4, 6, 6]
sz = [2, 1, 2, 1, 2, 1, 2, 1]

0 2
id = [0, 0, 0, 2, 4, 4, 6, 6]
sz = [4, 1, 2, 1, 2, 1, 2, 1]

4 6
id = [0, 0, 0, 2, 4, 4, 4, 6]
sz = [4, 1, 2, 1, 4, 1, 2, 1]

0 4
id = [0, 0, 0, 2, 0, 4, 4, 6]
sz = [8, 1, 2, 1, 4, 1, 2, 1]

Number of array access: 21
```

**1.5.5** Estimate min days requried for quick-find to solve dynamic connectivity problem with `10^<sup>9</sup>` sites and `10<sup>6</sup>` input pairs. Computer can execute `10<sup>9</sup>` instructions per second. Each iteration requires 10 instructions.

Considering intitialization negligible as init takes `10<sup>9</sup>`  for `id[]` + some none array vairables.

Each call to `union` requires 2 calls to `find`, making it `2\*10<sup>6</sup>` (# of inputs) which is negligible.

Every `union` makes `10<sup>9</sup>` accessess to `id[]` (its lenght), with 10 operations per loop totaling `10<sup>10</sup>`.

Since we call `union` `10<sup>6</sup>` times, we get a total of `10<sup>6</sup> * 10<sup>10</sup> = 10<sup>16</sup>`.

This means that it will take `10<sup>16</sup>/10<sup>9</sup>` seconds (number of operations / operaionts per second). This gives `10^<sup>7</sup>` seconds. Dividing  `10^<sup>7</sup>` by 86400 (seconds in a day) gives us at least 115 days.

**1.5.6** Repeat but with weighted quick uinon

Considering intitialization negligible as init takes `2 * 10<sup>9</sup>`  for `id[]`  and `sz[]` + some none array vairables.

Each call to `union` requires 2 calls to `find` with a complexity of `lg(10<sup>9</sup>) ~ 30`, multiplying by `10 ` (instructions per loop) we get `2 * 300` operations times `10<sup>6</sup>` inputs totaling `2 * 10<sup>8</sup> ~ `

Every `union` operation is constant, so we will ignore.

This means that it will take `6 * 10<sup>8</sup>/10<sup>9</sup>` seconds, totaling `
6 * 10<sup>-1</sup> = 0.6s`, meaning it takes less than a day.

**1.5.7** implement quick-union and quick-find

**1.5.8** Give a counter example for a why an implementation for `union` for quick-uninon is not correct: 
```
public void union(int p, int q)
    {
        if (connected(p, q)) return;
        // Rename p’s component to q’s name.
        for (int i = 0; i < id.length; i++)
           if (id[i] == id[p]) id[i] = id[q];
        count--; 
    }
```

Let's say we have an `id = [0 1 2 2]` and we call `union(2,1)`, this should in theory output `id = [0 1 1 1]`.

We first realize that `p = 2 & id[p] = 2`, similarly `q = 1 & id[q] = 1.`

1. `i = 0` and `id[0]=0 & id[0]!=id[p(2)]`, so we do nothing.
2. `i = 1` and `id[1]=1 & id[1]!=id[p(2)]`, so we do nothing.
3. `i = 2` and `id[2]=2 & id[2]==id[p(2)]`, so now `id[p] = id[q(1)]`.
4. `i = 3` and `id[3]=2 & id[3]!= id[p(1)]`, so we do nothing**!!** we should have changed this value, but we are not able as the comparison fails because we changed the value of `id[p]`.

That is why this implementation fails.

**1.5.9** Draw the tree corresponding to `id[] = [1 1 3 1 5 6 1 3 4 5]`. Can this be the result of running weighted quick-union? Explain why this is impossible or give a sequence of operations that results in this array.
```
     1
 0  3    6
   2 7   5
        4 9
        8
```
It is not possible: one fact about weighted quick union is that it's trees have a height of at most `lg(n)` with `n` bieng the number of sites in a given component. Our tree has a height of `4` and `lg(10) ~ 3.3 < 4`.

If we only focus on the tree given by `[1 6 5 4 9 8]` we have that `lg(6) < 3 <4` which further proves the above.

**1.5.10** In weighted quick-union algorithm, suppose we set `id[find(p)]` to `q` instead of `id[find(q)]`. Would the resulting algorithm be correct?

Yes, but it would increase the tree height, so the performance guarantee would be invalid.

**1.5.11** Implement weighted quick-union where you always change `id[]` entries for the smaller component to the identifier for the larger component. How does this change affect performance?

Given that `find` now is a constant function, given that we have to access the `id[]` at most two times, to find the root of any given node.

The implementation of `union` no longer costs `lg(N)`, as we have to check every entry in the `id[]` array, it is now of linear complexity.

TLDR; Performance is worse.



