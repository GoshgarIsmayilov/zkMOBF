def bellman_ford(bids):
    # Initialize network
    edges = []
    for idx, bid in enumerate(bids):
        token_from, amount_from, token_to, amount_to = bid
        weight = -1
        edges.append((token_from, token_to, weight, idx))

    nodes = set()
    for u, v, _, _ in edges:
        nodes.add(u)
        nodes.add(v)


    # Iterate Bellman-Ford
    cycles = []
    for start_node in nodes:
        # Initialize distances
        distances = {node: 999999 for node in nodes}
        predecessors = {node: None for node in nodes}
        bid_indices = {node: None for node in nodes}

        distances[start_node] = 0
        for _ in range(len(nodes) - 1):
            for u, v, weight, idx in edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u
                    bid_indices[v] = idx

                # print(start_node, u, v, idx, distances)

        # Detect cycles
        for u, v, weight, idx in edges:
            if distances[u] + weight < distances[v]:
                cycle = []
                visited = set()
                current = v

            # print(start_node, u, v, (distances[u] + weight < distances[v]))

                # Backtrack to find the cycle
                while current not in visited:
                    visited.add(current)
                    cycle.append(bid_indices[current])
                    current = predecessors[current]

                print(cycle)

                """ if cycle not in cycles:
                    cycles.append(cycle)

                # Remove edges in the cycle after storing it
                edges = [e for e in edges if e[3] not in cycle]
                break """ 

    return cycles


# Example bids
bids = [
    ["A", 3, "B", 3],
    ["B", 3, "A", 3],
    ["C", 1, "D", 1],
    ["D", 1, "E", 1],
    ["E", 1, "F", 1],
    ["F", 1, "G", 1],
    ["G", 1, "H", 1],
    ["H", 1, "C", 1],
]

bids = [
    ["A", 3, "B", 3],
    ["B", 3, "A", 3],
    ["C", 1, "D", 1],
]

# Find and print cycles
for cycle in bellman_ford(bids):
    print(cycle)
