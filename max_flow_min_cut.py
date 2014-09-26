import sys
from Queue import *

class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name 


class Edge:
    def __init__(self, v, w, c):
        self.v = v
        self.w = w
        self.c = c
        self.f = 0

    def add_flow(self, f):
        self.f += f

    def __repr__(self):
        return str(self.v.name) + " -- " + str(self.f) + "/" + str(self.c) + " -> " + str(self.w.name)


class Graph:
    def __init__(self, N, E):
        self.nodes = []
        self.edges = []
        self.adjacency_list = []

        for i in range(0, N):
            self.adjacency_list.append([])

    def addEdge(self, v_id,  w_id, c):
        v = self.nodes[v_id]
        w = self.nodes[w_id]
        e = Edge(v, w, c)

        self.edges.append(e)
        self.adjacency_list[v_id].append(e)


    def addNode(self, v):
        self.nodes.append(v)


def parse_data():
    data = sys.stdin.read().splitlines()
    N = int(data[0])
    nodes = data[1:N+1]
    M = int(data[N+1])
    
    g = Graph(N, M)
    for i, name in enumerate(nodes):
        g.addNode(Node(i, name))

    for d in data[N+2:]:
        d = d.split()
        v_id = int(d[0])
        w_id = int(d[1])
        c = int(d[2])
        g.addEdge(v_id, w_id, c)

    return g


def bfs(graph):
    source_egdes = graph.adjacency_list[0]
    frontier = Queue()
    frontier.put(source_egdes)
    while not frontier.empty():
        current_edge = frontier.get()
        print current_edge
        current_node = current_edge.w
        frontier.put(graph.adjacency_list[current_node.id])
        #print current_edge
        


g = parse_data()
bfs(g)


for e in g.edges:
    pass
    #print e