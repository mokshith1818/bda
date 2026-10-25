
# Girvan-Newman Algorithm

import networkx as nx

# Step 1: Create a graph
G = nx.Graph()

edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'C'),
    ('D', 'E'), ('D', 'F'), ('E', 'F'),
    ('C', 'D')
]

G.add_edges_from(edges)

print("Original edges:", list(G.edges()))

# Step 2: Calculate and remove edges
while nx.number_connected_components(G) == 1:

    # Calculate edge betweenness centrality
    centrality = nx.edge_betweenness_centrality(G)

    # Find the edge with highest centrality
    edge = max(centrality, key=centrality.get)

    print("Removing edge:", edge)
    G.remove_edge(*edge)

# Step 3: Display communities
communities = list(nx.connected_components(G))

print("\nCommunities:")
for i, community in enumerate(communities, 1):
    print("Community", i, ":", sorted(community))
