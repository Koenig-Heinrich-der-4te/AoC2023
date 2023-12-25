# https://adventofcode.com/2023/day/25
with open("25.txt") as f:
    raw_nodes = f.readlines()


nodes = {}
for line in raw_nodes:
    node, children = line.split(": ")
    nodes[node] = set(children.split())

for node, children in list(nodes.items()):
    for child in children:
        if child not in nodes:
            nodes[child] = {node}
        else:
            nodes[child].add(node)


edge_heat_map = {}


def run_around(start_node):
    # find how many nodes are connected to the start node
    visited = {start_node}
    to_visit = [start_node]
    while to_visit:
        node = to_visit.pop()
        for child in nodes[node]:
            if child not in visited:
                visited.add(child)
                to_visit.append(child)
    return len(visited)


def find(a, b):
    # find a path between the two nodes a and b
    visited = {a: None}
    to_visit = [a]
    while to_visit:
        node = to_visit.pop(0)
        children = list(nodes[node])
        for child in children:
            if child not in visited:
                visited[child] = node
                to_visit.append(child)
                if child == b:
                    to_visit = False  # dirty way to exit the loop
                    break
    # track back the path and increment the counter for each edge
    node = b
    while node != a:
        key = "/".join(sorted((node, visited[node])))
        edge_heat_map[key] = edge_heat_map.get(key, 0) + 1
        node = visited[node]
    return False


def is_done():
    # operation is completed if the correct edges to cut are found
    seperators = sorted(edge_heat_map.items(), key=lambda x: x[1], reverse=True)[:3]
    for seperator, _ in seperators:
        a, b = seperator.split("/")
        nodes[a].remove(b)
        nodes[b].remove(a)
    cluster_size = run_around(a)  # pass a random node
    # failed to find the correct edges
    if cluster_size == len(nodes):
        for seperator, _ in seperators:
            a, b = seperator.split("/")
            nodes[a].add(b)
            nodes[b].add(a)
        return False
    return True


# find the correct edges to cut by finding paths between all nodes
# and assuming the edges with most traffic are the ones connecting the two clusters
keys = list(nodes.keys())
for i, a in enumerate(keys):
    for b in keys[i + 1 :]:
        find(a, b)
    if is_done():
        break

cluster1 = run_around(a)  # pass a random node
cluster2 = len(nodes) - cluster1
print(f"{cluster1} * {cluster2} => {cluster1 * cluster2}")
