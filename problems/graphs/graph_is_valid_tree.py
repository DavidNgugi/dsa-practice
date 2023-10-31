from typing import List

# https://leetcode.com/problems/graph-valid-tree/
# https://www.lintcode.com/problem/178/

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to check whether these edges make up a valid tree.

# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the
# same as [1, 0] and thus will not appear together in edges.

# Examples

# Example 1:
# Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: true.

# Example 2:
# Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    """
    Time -> O(V+E)
    Space -> O(V+E)
    """
    # write your code here
    adjList = {i: [] for i in range(n)}

    for n1, n2 in edges:
        adjList[n1].append(n2)
        adjList[n2].append(n1)

    visited = set()

    def dfs(v, prev):
        # False means it has a cycle
        if v in visited:
            return False

        visited.add(v)

        for e in adjList[v]:
            if e == prev:
                continue
            if not dfs(e, v):
                return False
        return True

    # we need to have no cycles and to have visited all nodes to be a valid tree

    return dfs(0, -1) and len(visited) == n


if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    output = True

    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    output2 = False

    print(valid_tree(n, edges) == output)
    print(valid_tree(n2, edges2) == output2)
