# Algorithms and Data Structures

**Author:** Eva Makarova  
**Programming Language:** Python 3  

Read this in other languages: [Русский](README_RU.md)

---

## Repository Overview

This repository contains practical assignments, laboratory works, and reports for the "Algorithms and Data Structures" course.

---

## Laboratories and Reports

| No. | Assignment | Description / Topics | Report Link |
|---|---|---|---|
| 1 | Laboratory Work 1 | **Greedy Algorithms. Dynamic Programming No. 2** | [Laboratory Work No. 1](#lab1) |
| 2 | Laboratory Work 2 | **Binary Search Trees** | [Laboratory Work No. 2](#lab2) |
| 3 | Laboratory Work 3 | **Graphs & Graph Algorithms** | [Laboratory Work No. 3](#lab3) |
| 4 | Laboratory Work 4 | **Substring Search Algorithms** | [Laboratory Work No. 4](#lab4) |


<a id="lab1">
</a>

Laboratory Work No. 1: Greedy Algorithms. Dynamic Programming No. 2
---

## Table of Contents
1. [Assigned Variant Tasks](#assigned-variant-tasks)
   - [Task #1. Maximum Loot Value](#task-1-maximum-loot-value)
   - [Task #6. Maximum Salary](#task-6-maximum-salary)
   - [Task #16. The Salesman](#task-16-the-salesman)
   - [Task #15. Bracket Removal](#task-15-bracket-removal)
   - [Task #18. Cafe](#task-18-cafe)
2. [Additional Tasks](#additional-tasks)
   - [Task #22. Pretty Patterns](#task-22-pretty-patterns)
   - [Task #19. Matrix Chain Multiplication](#task-19-matrix-chain-multiplication)
   - [Task #21. Fool Card Game](#task-21-fool-card-game)
   - [Task #8. Lecture Schedule](#task-8-lecture-schedule)
3. [Conclusion](#conclusion)

---

## Assigned Variant Tasks

### Task #1. Maximum Loot Value
* **Goal:** Implement an algorithm to solve the Fractional Knapsack problem to maximize the total value of items that can fit into a bag of capacity $W$.
* **Input Format (`input.txt`):** 
  * First line: $n$ (number of items) and $W$ (knapsack capacity).
  * Next $n$ lines: Pairs of integers $p_i$ (price) and $w_i$ (weight) for each item.
* **Constraints:** $1 \le n \le 10^3$, $0 \le W \le 2 \cdot 10^6$, $0 \le p_i \le 2 \cdot 10^6$, $0 \le w_i \le 2 \cdot 10^6$.
* **Output Format (`output.txt`):** The maximum value of item fractions fitting in the bag, printed with at least 4 decimal places (absolute error $\le 10^{-3}$).
* **Approach:** Greedy approach — sort items by unit price ($p_i / w_i$) in descending order and greedily fill the knapsack.

---

### Task #6. Maximum Salary
* **Goal:** Compose the largest possible number (salary) by concatenating a given list of single- and multi-digit positive integers.
* **Input Format (`input.txt`):** 
  * First line: $n$ (number of integers).
  * Second line: $n$ positive integers separated by spaces.
* **Constraints:** $1 \le n \le 100$, each integer $\le 10^3$.
* **Output Format (`output.txt`):** The largest number that can be formed.
* **Approach:** Custom comparator sorting — two numbers $A$ and $B$ are compared such that $A$ comes before $B$ if $A + B > B + A$ (string concatenation).

---

### Task #16. The Salesman (Travelling Salesperson Problem)
* **Goal:** Find the shortest path visiting all given vertices (cities) exactly once and returning to the starting vertex in a weighted graph.
* **Input Format (`input.txt`):** 
  * First line: $n$ (number of cities).
  * Next $n$ lines: $n \times n$ adjacency matrix representing distances between cities.
* **Constraints:** $1 \le n \le 18$, edge weights are non-negative integers $\le 10^9$.
* **Output Format (`output.txt`):** Minimum distance to complete the TSP tour.
* **Approach:** Dynamic Programming with Bitmasking — state representation `dp[mask][u]` stores the minimum distance visiting subset `mask` ending at vertex `u` with time complexity $O(n^2 \cdot 2^n)$.

---

### Task #15. Bracket Removal
* **Goal:** Given a string of brackets (`()`, `[]`, `{}`), find the maximum length of a correct bracket subsequence that can be formed by removing the minimum number of characters.
* **Input Format (`input.txt`):** A string consisting of brackets.
* **Constraints:** String length $N \le 100$.
* **Output Format (`output.txt`):** The maximum length of a valid bracket sequence / resulting sequence.
* **Approach:** Interval Dynamic Programming — `dp[i][j]` computes the optimal solution for substring from index $i$ to $j$.

---

### Task #18. Cafe
* **Goal:** Calculate the minimum cost to purchase lunches over $N$ days given a coupon system (a coupon for a free lunch is granted for purchases $> 100$ rubles).
* **Input Format (`input.txt`):** 
  * First line: $N$ (number of days).
  * Next $N$ lines: Cost of lunch on day $i$.
* **Constraints:** $0 \le N \le 100$, lunch price $\le 300$.
* **Output Format (`output.txt`):** Total minimum spent, number of unused coupons remaining, and the specific days on which coupons were spent.
* **Approach:** Dynamic Programming — `dp[day][coupons]` tracks the minimum total cost at a given day with a specific count of unused coupons, followed by state reconstruction to list coupon usage days.

---

## Additional Tasks

### Task #22. Pretty Patterns
* **Goal:** Calculate the number of "pretty" grid patterns of size $M \times N$ with $2 \times 2$ subgrids not consisting entirely of a single color.
* **Input Format (`input.txt`):** Two integers $M$ and $N$.
* **Constraints:** $1 \le M \cdot N \le 30$, $M \le N$.
* **Output Format (`output.txt`):** The total number of valid pretty patterns.
* **Approach:** Profile Dynamic Programming / Transfer Matrix approach — tracking valid transitions between adjacent column profiles of mask length $M$.

---

### Task #19. Matrix Chain Multiplication
* **Goal:** Determine the optimal parenthesization of a product of matrices to minimize the total number of scalar multiplications.
* **Input Format (`input.txt`):** 
  * First line: $n$ (number of matrices).
  * Second line: $n + 1$ integers defining dimensions $p_0, p_1, \dots, p_n$.
* **Constraints:** $1 \le n \le 500$, dimensions $\le 100$.
* **Output Format (`output.txt`):** Minimum number of scalar multiplications required.
* **Approach:** Interval Dynamic Programming — `dp[i][j] = min_{k}(dp[i][k] + dp[k+1][j] + p_{i-1}p_k p_j)$.

---

### Task #21. Fool Card Game
* **Goal:** Determine whether a attacker hand can successfully beat a defender hand in a simplified Russian card game ("Fool") given a designated trump suit.
* **Input Format (`input.txt`):** Card hands and trump suit specification.
* **Constraints:** Standard deck subset sizes.
* **Output Format (`output.txt`):** `YES` or `NO` along with the matching card pairs if winning strategy exists.
* **Approach:** Bipartite Matching / Greedy Card Selection.

---

### Task #8. Lecture Schedule
* **Goal:** Select the maximum number of non-overlapping lecture intervals (Interval Scheduling Problem).
* **Input Format (`input.txt`):** 
  * First line: $n$ (number of lectures).
  * Next $n$ lines: Start and end times $[s_i, f_i]$.
* **Constraints:** $1 \le n \le 10^5$, timestamps $\le 10^9$.
* **Output Format (`output.txt`):** Maximum count of non-overlapping lectures.
* **Approach:** Greedy Algorithm — sort intervals by end time $f_i$ and iteratively select the earliest finishing compatible lecture.

---

## Conclusion

In this laboratory work, key algorithmic paradigms were analyzed and implemented, focusing on **Greedy Algorithms** and **Dynamic Programming (Part 2)**:

1. **Greedy Optimization Efficiency:** Demonstrated that greedy strategies yield globally optimal results for structural problems with optimal substructure and greedy-choice property (e.g., Fractional Knapsack, Interval Scheduling, Custom Sorting for Maximum Salary) within low time complexities ($O(n \log n)$).
2. **Advanced Dynamic Programming Techniques:**
   - **Interval DP:** Successfully applied to string structure problems (Bracket Removal) and matrix multiplication chain optimization.
   - **DP with Bitmasks:** Reduced exponential brute-force complexity $O(n!)$ of the Travelling Salesperson Problem (TSP) down to $O(n^2 \cdot 2^n)$, making exact solutions feasible for $n \le 18$.
   - **Profile DP & State Tracking:** Solved spatial constraint problems (Pretty Patterns) and stateful transaction optimizations (Cafe problem with coupon recovery via backtracking).
3. **Comparative Analysis:** Evaluated trade-offs between exact DP techniques vs. greedy heuristics in terms of optimality guarantees and computational constraints across all 9 target tasks.

<a id="lab2">
</a>

Laboratory Work No. 2: Binary Search Trees
---

## Table of Contents
1. [Assigned Variant Tasks](#assigned-variant-tasks)
   - [Task #1. Tree Traversals](#task-1-tree-traversals)
   - [Task #12. Check Balanced](#task-12-check-balanced)
   - [Task #14. Insertion into AVL Tree](#task-14-insertion-into-avl-tree)
2. [Additional Tasks](#additional-tasks)
   - [Task #5. Simple Binary Search Tree](#task-5-simple-binary-search-tree)
   - [Task #13. I'm Making a Left Rotation...](#task-13-im-making-a-left-rotation)
   - [Task #15. Deletion from AVL Tree](#task-15-deletion-from-avl-tree)
   - [Task #18. Rope](#task-18-rope)
3. [Conclusion](#conclusion)

---

## Assigned Variant Tasks

### Task #1. Tree Traversals
* **Goal:** Implement the three primary depth-first traversal algorithms for a given binary tree: In-Order, Pre-Order, and Post-Order.
* **Input Format (`input.txt`):** 
  * First line: $n$ (number of nodes). Nodes are indexed from $0$ to $n - 1$, with node $0$ as the root.
  * Next $n$ lines: Key $K_i$, left child index $L_i$, and right child index $R_i$ for each node ($-1$ if no child).
* **Constraints:** $1 \le n \le 10^5$, $0 \le K_i \le 10^9$, $-1 \le L_i, R_i \le n - 1$.
* **Output Format (`output.txt`):** Three lines containing the keys traversed in In-Order, Pre-Order, and Post-Order, respectively.
* **Approach:** Recursive or iterative depth-first search (DFS) traversal over the implicit pointer array representation of the tree.

---

### Task #12. Check Balanced
* **Goal:** Determine whether a given binary search tree is height-balanced (i.e., for every node, the height difference between its left and right subtrees is at most 1).
* **Input Format (`input.txt`):** 
  * First line: $n$ (number of nodes).
  * Next $n$ lines: Key $K_i$, left child index $L_i$, and right child index $R_i$ for each node.
* **Constraints:** $0 \le n \le 10^5$, $-1 \le L_i, R_i \le n - 1$.
* **Output Format (`output.txt`):** `YES` if the tree is balanced, `NO` otherwise.
* **Approach:** Bottom-up recursive post-order depth check: compute node heights while short-circuiting if an unbalanced subtree ($\vert{}h_{left} - h_{right}\vert{} > 1$) is encountered, operating in $O(n)$ time.

---

### Task #14. Insertion into AVL Tree
* **Goal:** Insert a new key into an existing valid AVL tree while maintaining the AVL balance invariant via tree rotations.
* **Input Format (`input.txt`):** 
  * First line: $n$ (number of nodes prior to insertion).
  * Next $n$ lines: Key $K_i$, left child index $L_i$, and right child index $R_i$.
  * Last line: Key $X$ to be inserted.
* **Constraints:** $0 \le n \le 10^5$, all keys fit in standard 32-bit signed integers.
* **Output Format (`output.txt`):** Output the modified AVL tree structure after inserting $X$ in the same index-based format.
* **Approach:** Standard BST insertion followed by bottom-up height update and balancing using single (LL, RR) or double (LR, RL) rotations.

---

## Additional Tasks

### Task #5. Simple Binary Search Tree
* **Goal:** Implement a fundamental Binary Search Tree (BST) supporting basic operations: element insertion, element deletion, existence search, and finding next/previous elements.
* **Input Format (`input.txt`):** Sequence of operations (`insert x`, `delete x`, `exists x`, `next x`, `prev x`).
* **Constraints:** Up to $10^5$ operations; element keys fit in 32-bit signed integers.
* **Output Format (`output.txt`):** Results for `exists` (`true`/`false`), and keys (or `none`) for `next` / `prev` operations.
* **Approach:** Node-based pointer BST with dynamic memory management or array-based storage, featuring standard BST traversal and deletion via in-order successor swapping.

---

### Task #13. I'm Making a Left Rotation...
* **Goal:** Perform a single left rotation on a specified node of a binary search tree and output the resulting tree structure.
* **Input Format (`input.txt`):** 
  * First line: $n$ (number of nodes).
  * Next $n$ lines: Node description triplets ($K_i, L_i, R_i$).
* **Constraints:** $1 \le n \le 10^5$.
* **Output Format (`output.txt`):** Node structural list of the transformed tree after applying a left rotation at the root.
* **Approach:** Re-link pointers such that the root's right child becomes the new root, and the right child's left subtree becomes the old root's new right subtree in $O(1)$ time.

---

### Task #15. Deletion from AVL Tree
* **Goal:** Delete a specified key from an AVL tree and rebalance the tree to maintain the AVL height invariant.
* **Input Format (`input.txt`):** 
  * First line: $n$ (number of nodes).
  * Next $n$ lines: Node structural triplets ($K_i, L_i, R_i$).
  * Last line: Key $X$ to delete.
* **Constraints:** $1 \le n \le 10^5$.
* **Output Format (`output.txt`):** The resulting AVL tree representation after deletion.
* **Approach:** Recursive BST deletion (replacing node with its maximum element in left subtree or minimum in right subtree) followed by propagating height updates and balance factor corrections (rotations) up to the root.

---

### Task #18. Rope
* **Goal:** Implement a Rope data structure based on balanced search trees (Splay or Treap / Implicit Treap) to efficiently perform string slicing and re-ordering operations.
* **Input Format (`input.txt`):** 
  * First line: Initial string $S$.
  * Second line: $q$ (number of query operations).
  * Next $q$ lines: Range indices $i, j$ and insertion position $k$, representing cutting substring $S[i..j]$ and inserting it after index $k$.
* **Constraints:** String length $\vert{}S\vert{} \le 3 \cdot 10^5$, $q \le 10^5$.
* **Output Format (`output.txt`):** The final string after applying all $q$ cut-and-paste transformations.
* **Approach:** Implicit Treap (Treap by implicit key / size) supporting subtree `split` and `merge` operations in $O(\log N)$ time per query.

---

## Conclusion

In this laboratory work, foundational and advanced search tree data structures were studied and implemented, focusing on **Binary Search Trees (BST)**, **Self-Balancing Trees (AVL)**, and **Augmented Implicit Trees (Rope / Treap)**:

1. **Tree Traversals & Structural Integrity:** Demonstrated depth-first search techniques (In-Order, Pre-Order, Post-Order) and efficient $O(n)$ bottom-up balance checking algorithms for arbitrary binary trees.
2. **Self-Balancing Invariants (AVL Trees):**
   - Applied single (LL, RR) and double (LR, RL) rotations to maintain logarithmic height guarantees ($h \le 1.44 \log_2 n$).
   - Implemented dynamic node insertion and deletion in $O(\log n)$ time while ensuring structural invariants across modifications.
3. **Implicit Search Trees & Advanced Text Processing:**
   - Implemented an implicit key Treap (Rope) to perform array/string substring extraction and re-insertion in $O(\log n)$ per query.
   - Reduced the naive array copy complexity from $O(n \cdot q)$ down to $O(q \log n)$, making large-scale dynamic text manipulations computationally feasible.

<a id="lab3">
</a>

Laboratory Work No. 3: Graphs
---

## Table of Contents
1. [Assigned Variant Tasks](#assigned-variant-tasks)
   - [Task #1. Maze](#task-1-maze)
   - [Task #10. Optimal Currency Exchange](#task-10-optimal-currency-exchange)
   - [Task #14. Buses](#task-14-buses)
2. [Additional Tasks](#additional-tasks)
   - [Task #13. Garden Beds](#task-13-garden-beds)
   - [Task #15. Heroes](#task-15-heroes)
   - [Task #17. Weak K-Connectivity](#task-17-weak-k-connectivity)
   - [Task #18. Road Construction](#task-18-road-construction)
   - [Task #19. Clustering](#task-19-clustering)
3. [Conclusion](#conclusion)

---

## Assigned Variant Tasks

### Task #1. Maze
* **Goal:** Determine whether a path exists between two given vertices $u$ and $v$ in an undirected graph representing a maze.
* **Input Format (`input.txt`):** 
  * Undirected graph with $n$ vertices and $m$ edges.
  * The last line contains two vertices $u$ and $v$.
* **Constraints:** $2 \le n \le 10^3$, $1 \le m \le 10^3$, $1 \le u, v \le n$, $u \neq v$.
* **Output Format (`output.txt`):** Print `1` if a path exists between $u$ and $v$, otherwise print `0`.
* **Approach:** Breadth-First Search (BFS) or Depth-First Search (DFS) / Disjoint Set Union (DSU) to check connectivity between vertices $u$ and $v$.

---

### Task #10. Optimal Currency Exchange
* **Goal:** Find the maximum amount of target currency that can be obtained starting from a given initial currency, considering exchange rates and transaction fees, or detect negative/arbitrage cycles.
* **Input Format (`input.txt`):** Graph representation of currency exchange rates and transaction fees between different currencies.
* **Constraints:** Standard graph boundaries for currency exchange models.
* **Output Format (`output.txt`):** Maximum achievable currency amount or an indicator for arbitrage/infinite profit possibilities.
* **Approach:** Bellman-Ford Algorithm or Floyd-Warshall Algorithm modified for product/rate maximization to detect negative cycles (arbitrage opportunities) and compute shortest paths in log-transformed weight spaces.

---

### Task #14. Buses
* **Goal:** Find the minimum time required to travel from a starting city $S$ to a destination city $F$ using a scheduled bus system where routes have specific departure and arrival times.
* **Input Format (`input.txt`):** 
  * First line: Number of cities $N$, start city $S$, finish city $F$.
  * Subsequent lines: Bus schedule details including origin, departure time, destination, and arrival time.
* **Constraints:** $1 \le N \le 10^5$, edge schedule constraints.
* **Output Format (`output.txt`):** The earliest possible arrival time at city $F$, or `-1` if unreachable.
* **Approach:** Modified Dijkstra's Algorithm taking into account time-dependent edge weights (waiting time for bus departures).

---

## Additional Tasks

### Task #13. Garden Beds
* **Goal:** Count the number of connected components (garden beds) in a 2D grid representation of a plot of land.
* **Input Format (`input.txt`):** Grid dimensions followed by a 2D matrix representing garden bed layout (`#` for land, `.` for water).
* **Constraints:** Standard grid dimensions ($M \times N \le 10^6$).
* **Output Format (`output.txt`):** Total count of connected components.
* **Approach:** Connected Components Search using Flood Fill (DFS/BFS) on a grid graph (4-directional or 8-directional traversal).

---

### Task #15. Heroes
* **Goal:** Determine the optimal path or strategy for heroes traversing a graph with weighted edges/nodes subject to resource constraints or strategic conditions.
* **Input Format (`input.txt`):** Weighted graph parameters and hero attributes/constraints.
* **Constraints:** Graph processing limits.
* **Output Format (`output.txt`):** Optimal path cost or maximum score achievable by the hero.
* **Approach:** Shortest Path Algorithm (Dijkstra/A*) combined with state space representation (DP on Graphs).

---

### Task #17. Weak K-Connectivity
* **Goal:** Evaluate the weak $K$-connectivity properties of a directed graph or find the maximum $K$ for which the graph remains $K$-connected.
* **Input Format (`input.txt`):** Directed graph adjacency list or matrix and parameter $K$.
* **Constraints:** Standard directed graph limits.
* **Output Format (`output.txt`):** Connectivity verification status or calculated metrics.
* **Approach:** Graph Traversal (Tarjan's or Kosaraju's Algorithm) applied to the underlying undirected graph to determine component structures and vertex/edge cut properties.

---

### Task #18. Road Construction
* **Goal:** Connect all cities with the minimum total road construction cost (Minimum Spanning Tree).
* **Input Format (`input.txt`):** Coordinates of cities or pairwise distances between vertices.
* **Constraints:** $1 \le N \le 10^4$.
* **Output Format (`output.txt`):** Minimum total length/cost of constructed roads.
* **Approach:** Prim's Algorithm or Kruskal's Algorithm using Disjoint Set Union (DSU) to construct a Minimum Spanning Tree (MST).

---

### Task #19. Clustering
* **Goal:** Partition a set of points or vertices into $K$ clusters such that the minimum distance between any pair of points in different clusters is maximized.
* **Input Format (`input.txt`):** Set of points/graph vertices and target cluster count $K$.
* **Constraints:** Cluster count $K \le N \le 10^3$.
* **Output Format (`output.txt`):** The maximum possible minimum inter-cluster distance rounded to required precision.
* **Approach:** Kruskal's MST-based Clustering — build an MST and remove the $K-1$ largest edges to form $K$ optimal clusters.

---

## Conclusion

In this laboratory work, structural and algorithmic properties of **Graph Theory** were analyzed, implemented, and evaluated:

1. **Traversal & Connectivity:** Demonstrated that Breadth-First Search (BFS) and Depth-First Search (DFS) provide optimal linear time $O(V + E)$ solutions for basic reachability (Maze task) and component analysis (Garden Beds).
2. **Shortest Path Algorithms & Scheduling:**
   - Evaluated **Dijkstra's Algorithm** for time-dependent networks (Buses task), adapting edge weight evaluations dynamically to schedule constraints.
   - Applied **Bellman-Ford Algorithm** to handle multi-currency trade optimizations and identify negative weight cycles (arbitrage opportunities).
3. **Spanning Trees & Clustering Optimization:**
   - Implemented **Kruskal's and Prim's Algorithms** using efficient Disjoint Set Union (DSU) structures to solve Minimum Spanning Tree (MST) problems (Road Construction).
   - Applied MST edge-cutting techniques to achieve optimal spacing in metric $K$-clustering (Clustering task).
4. **Complexity & Performance:** Verified theoretical time and space complexities against empirical execution metrics, ensuring performance compliance within memory (512 MB) and time limits.

<a id="lab4">
</a>

Laboratory Work No. 4: Substrings
---

## Table of Contents
1. [Assigned Variant Tasks](#assigned-variant-tasks-1)
   - [Task #1. Naive Substring Search](#task-1-naive-substring-search)
   - [Task #4. Substring Equality](#task-4-substring-equality)
   - [Task #6. Z-Function](#task-6-z-function)
2. [Additional Tasks](#additional-tasks-1)
   - [Task #2. Map (Pattern Matching with Wildcards)](#task-2-map-pattern-matching-with-wildcards)
   - [Task #7. Longest Common Substring](#task-7-longest-common-substring)
3. [Conclusion](#conclusion-1)

---

## Assigned Variant Tasks

### Task #1. Naive Substring Search
* **Goal:** Find all occurrences of a pattern string $p$ in a text string $t$ using exact pattern matching.
* **Input Format (`input.txt`):** 
  * First line: Pattern string $p$.
  * Second line: Text string $t$.
* **Constraints:** $1 \le \vert{}p\vert{} \le 10^3$, $1 \le \vert{}t\vert{} \le 10^5$.
* **Output Format (`output.txt`):** Total count of occurrences followed by 1-based starting indices of each match.
* **Approach:** Brute-force (naive) sliding window approach — sliding a window of length $\vert{}p\vert{}$ across $t$ and performing character-by-character comparisons in $O(\vert{}p\vert{} \cdot (\vert{}t\vert{} - \vert{}p\vert{} + 1))$ time.

---

### Task #4. Substring Equality
* **Goal:** Efficiently determine whether two substrings $t[a \dots a+l-1]$ and $t[b \dots b+l-1]$ of equal length $l$ are identical across multiple query requests.
* **Input Format (`input.txt`):** 
  * First line: Text string $t$.
  * Second line: $q$ (number of queries).
  * Next $q$ lines: Triplets of integers $a, b, l$ specifying 0-based starting positions $a, b$ and substring length $l$.
* **Constraints:** $1 \le \vert{}t\vert{} \le 5 \cdot 10^5$, $1 \le q \le 10^5$.
* **Output Format (`output.txt`):** `Yes` if substrings are identical, `No` otherwise for each query.
* **Approach:** Polynomial Rolling Hash with precomputed prefix hashes and powers of a base modulo $M$, enabling $O(1)$ substring hash extraction via $H(pos, l) = (H[pos + l] - H[pos] \cdot P^l) \pmod M$.

---

### Task #6. Z-Function
* **Goal:** Compute the Z-array for a given string $s$ of length $n$.
* **Input Format (`input.txt`):** Single line containing string $s$.
* **Constraints:** $1 \le n \le 10^6$, string consists of lowercase English letters.
* **Output Format (`output.txt`):** Space-separated values of the Z-array $Z[0], Z[1], \dots, Z[n-1]$.
* **Approach:** Linear time Z-algorithm keeping track of the rightmost matched segment $[L, R]$ to reuse previously computed Z-values and bound total character comparisons to $O(n)$.

---

## Additional Tasks

### Task #2. Map (Pattern Matching with Wildcards)
* **Goal:** Perform 2D matrix/grid pattern matching or wildcard-enabled pattern search across text structures.
* **Input Format (`input.txt`):** Grid dimensions and 2D character arrays for both the target map and pattern matrix.
* **Constraints:** Grid sizes up to $10^3 \times 10^3$.
* **Output Format (`output.txt`):** Coordinates of pattern occurrences in the 2D matrix.
* **Approach:** 2D Polynomial Hashing / Automata-based row-by-row Knuth-Morris-Pratt (KMP) matching to achieve optimal linear-space searching.

---

### Task #7. Longest Common Substring
* **Goal:** Find the longest contiguous substring present in two given strings $s_1$ and $s_2$.
* **Input Format (`input.txt`):** Two lines containing strings $s_1$ and $s_2$.
* **Constraints:** $1 \le \vert{}s_1\vert{}, \vert{}s_2\vert{} \le 10^5$.
* **Output Format (`output.txt`):** The maximum length of a common substring and optionally the substring itself.
* **Approach:** Binary Search on Answer combined with Polynomial Hashing / Suffix Automaton — checking candidate length $k$ using hash set lookups in $O((\vert{}s_1\vert{} + \vert{}s_2\vert{}) \log(\min(\vert{}s_1\vert{}, \vert{}s_2\vert{})))$ time.

---

## Conclusion

In this laboratory work, efficient algorithms and data structures for **String Processing and Substring Search** were investigated and evaluated:

1. **Exact & Naive Matching Limitations:** Analyzed the performance bounds of naive pattern matching ($O(\vert{}p\vert{} \cdot \vert{}t\vert{})$) and established the necessity of advanced preprocessing techniques for large-scale text strings.
2. **Hash-Based Acceleration:**
   - Applied **Polynomial Rolling Hashing** to answer range equality queries in constant time $O(1)$ after $O(n)$ preprocessing.
   - Leveraged binary search over hash sets to solve the Longest Common Substring problem in sub-quadratic time $O(n \log n)$.
3. **Linear-Time String Processing:** Implemented the **Z-Algorithm** to compute prefix-suffix matches in strict linear time $O(n)$, avoiding redundant character comparisons through sliding segment bounds $[L, R]$.
4. **Performance Measurement:** Benchmarked implementation runtime and peak memory usage across all tasks using custom performance monitoring utilities (`time` and `tracemalloc` decorators).