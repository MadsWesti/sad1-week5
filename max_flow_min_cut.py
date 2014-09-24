import sys


def parse_data():
    data = sys.stdin.read().splitlines()
    N = int(data[0])
    nodes = data[1:N+1]
    M = int(data[N+1])
    
    arcs = {}
    for d in data[N+2:]:
        d = d.split()
        a = int(d[0])
        b = int(d[1])
        c = int(d[2])
        arcs[a,b] = c

    return N, M, nodes, arcs

N, M, nodes, arcs = parse_data()
