from pprint import pprint


class GraphAdjMatrix:
    def __init__(self) -> None:
        self.graph = []

    def build_graph(self, nodes):
        for i in range(nodes):
            self.graph.append([0 for j in range(nodes)])

    def add_edge(self, v1, v2):
        if v1 == v2:
            print(f"same vertex {v1} and {v2}")
            return
        self.graph[v1][v2] = 1
        self.graph[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.graph[v1][v2] == 0:
            print(f"No edge between {v1} and  {v2}")
            return
        self.graph[v1][v2] = 0
        self.graph[v2][v1] = 0

    def display(self):
        pprint(self.graph)
        for i in range(len(self.graph)):
            for j in range(i):
                print(f"{self.graph[i][j]} -> {self.graph[j][i]}")


class GraphAdjList:
    def __init__(self) -> None:
        self.graph = {}

    def build_graph(self, nodes):
        pass

    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.graph[v1] = [v2]
        else:
            if v2 not in self.graph[v1]:
                self.graph[v1].append(v2)
            else:
                print(f"vertex {v2} alrady has an edge with {v1}")

    def remove_edge(self, v1, v2):
        if v1 not in self.graph:
            print(f"No vertex {v1} in graph")
        else:
            if v2 not in self.graph[v1]:
                print(f"No vertex {v2} connected to vertex {v1}")
            else:
                index = self.graph[v1].index(v2)
                self.graph[v1].remove(index)

    def display(self):
        pass


def bfs(self, graph):
    # use queue and visited set or update in-place
    # O(n)
    pass


def dfs(self, graph):
    # use recursion and backtracking
    # O(logn)
    pass


def union_find(self, graph):
    # O(nlogn)
    pass


def topological_sort(self, graph):
    # use dfs, directed acyclical graph, no cycles
    # can have multiple orders
    # O(n)
    # use hashset
    pass


def djikstras_algorithm(self, graph):
    # O(ElogV)
    # heap/priority queue
    # check minimum weights of edges for each vertex
    pass


def prims_minimum_spanning_tree(self):
    pass


def kruskals_minimum_spanning_tree(self):
    pass


def floyd_warshall_algorithm(self):
    pass


if __name__ == "__main__":
    g = GraphAdjMatrix()
    g.build_graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 0)
    g.display()
