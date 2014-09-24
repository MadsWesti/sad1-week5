import sys


def parse_data():
    data = sys.stdin.read().splitlines()
    N = int(data[0])
    nodes = data[1:N+1]
    M = int(data[N+1])
    
    arcs = {}
    for d in data[N+2:]:
        d = d.split()
        arcs[int(d[0]), int(d[1])] = int(d[2])

    return N, M, nodes, arcs

N, M, nodes, arcs = parse_data()
