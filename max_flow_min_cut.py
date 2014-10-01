import sys
from Queue import *
from operator import attrgetter


class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.visited = False


class Edge:
    def __init__(self, u, v, capacity, reverse=None):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0
        self.residual_capacity = self.capacity - self.flow

        if not reverse:
            self.reverse = Edge(v, u, capacity, self)
        else:
            self.reverse = reverse

    def add_flow(self, flow):
        self.flow += flow
        self.reverse.flow -= flow
        self.residual_capacity = self.capacity - self.flow
        self.reverse.residual_capacity = self.reverse.capacity \
            - self.reverse.flow

    def __repr__(self):
        return str(self.u.id) + "-->" + str(self.v.id) + " - " \
            + str(self.flow) + "/" + str(self.capacity)


class Graph:
    def __init__(self, N, M):
        self.nodes = []
        self.adjacency_list = {}
        self.A = []

    def add_edge(self, u_id, v_id, capacity, s_or_t=0):
        u = self.nodes[u_id]
        v = self.nodes[v_id]
        if capacity == -1:
            capacity = float("inf")
        e = Edge(u, v, capacity)

        self.adjacency_list[u].append(e)
        if not s_or_t:
            self.adjacency_list[v].append(e.reverse)

    def add_node(self, u):
        self.nodes.append(u)
        self.adjacency_list[u] = []

    def max_flow(self):
        f = 0
        while True:
            P = self.find_path(self.nodes[0], self.nodes[-1], [])
            if not P:
                break
            self.augment(f, P)

        for edge in self.adjacency_list[self.nodes[0]]:
            f += edge.flow

        return f

    def augment(self, f, P):
        b = self.bottleneck(P)
        for edge in P:
            edge.add_flow(b)

    def bottleneck(self, P):
        min_residual_capacity = min(P, key=attrgetter('residual_capacity'))\
            .residual_capacity
        return min_residual_capacity

    def find_path(self, source, sink, path):
        if source == sink:
            self.A = []
            self.A.append(self.nodes[0])  # Adding the source node

            # Resetting the visited booleans
            for node in self.nodes:
                node.visited = False
            return path

        for edge in self.adjacency_list[source]:
            node = edge.v
            if edge.residual_capacity > 0 and edge not in path \
                and not node.visited:
                self.A.append(edge.v)
                node.visited = True
                result = self.find_path(edge.v, sink, path + [edge])
                if result is not None:
                    return result


def parse_data():
    data = sys.stdin.read().splitlines()
    N = int(data[0])
    nodes = data[1:N + 1]
    M = int(data[N + 1])
    edges = data[N + 2:]

    g = Graph(N, M)

    for i, name in enumerate(nodes):
        g.add_node(Node(i, name))

    for e in edges:
        e = e.split()
        u_id = int(e[0])
        v_id = int(e[1])
        capacity = int(e[2])
        # If source or sink, send a true parameter to add_edge method
        # so as to not create the reverse edge
        if u_id == 0 or u_id == N - 1 or v_id == 0 or v_id == N - 1:
            g.add_edge(u_id, v_id, capacity, 1)
        else:
            g.add_edge(u_id, v_id, capacity)

    return g


g = parse_data()
print "Max flow is: " + str(g.max_flow())
print "\nEdges in min cut are:"
min_cut_capacity = 0

# Calculating the min cut
for node in g.A:
    for edge in g.adjacency_list[node]:
        if edge.u in g.A and edge.v not in g.A:
            print edge
            mcc += edge.capacity

print "\nMin cut is: " + str(min_cut_capacity)
