from minheap import MinHeap

inputs = open('input.txt')
s = inputs.readline().strip('\n').split(' ')

N = int(s[0]) # number of nodes
E = int(s[1]) # number of edges
src = s[2]    # source node

inputs = inputs.readlines()
inputs = [ x.strip('\n').split(' ') for x in inputs ]

graph = [
    [] for _ in range(N)
]

# to convert letters to numbers
index = 0
mapping = {}

for u, v, w in inputs:
    # give u and v a number
    if u not in mapping:
        mapping[u] = index
        index += 1

    if v not in mapping:
        mapping[v] = index
        index += 1

    # add the edge to the graph
    graph[mapping[u]].append((mapping[v], int(w)))
    graph[mapping[v]].append((mapping[u], int(w)))

# reverse the mapping
rmapping = { val : key for key, val in mapping.items() }

src = mapping[src]

def print_so_far():
    for i in range(N):
        offset = 4 if costs[i] == 10000 else costs[i]//10+4
        print('{0:<{1}}'.format(rmapping[i], offset), end='')
    print()

    for i in range(N):
        if costs[i] == 10000:
            print('inf', end=' ')
        else:
            print('{},{}'.format(costs[i], rmapping[parent[i]]), end = ' ')
    print()

# dijkstra part
parent  = [ i for i in range(N) ]
visited = [ False for _ in range(N) ]
costs   = [ 10000 for _ in range(N) ]
heap    = MinHeap() # for maintaining min cost element

#initalization
costs[src] = 0
heap.insert((0, src))

NN = ''
while not heap.empty():
    cw, cur = heap.poll()
    visited[cur] = True

    for v, w in graph[cur]:
        if not visited[v] and costs[v] > costs[cur] + w:
            costs[v] = costs[cur] + w
            heap.insert((costs[v], v))
            parent[v] = cur

    NN += rmapping[cur]
    print(NN)
    print_so_far()
