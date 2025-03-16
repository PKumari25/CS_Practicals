from collections import defaultdict

# Creating an empty graph
graph = defaultdict(list)

# Function to add an edge
def addEdge(graph, u, v):
    graph[u].append(v)

# Function to delete an edge
def removeEdge(graph, u, v):
    if v in graph[u]:
        graph[u].remove(v)

# Function to traverse and print the graph
def traverseGraph(graph):
    for node in graph:
         print(node, "->", graph[node] if graph[node] else "No connections")

# Function to generate edges
def generate_edges(graph):
    edges = []
    
    # For each node in graph
    for node in graph:
        # For each neighbour node of a single node
        for neighbour in graph[node]:
            # If edge exists then append
            edges.append((node, neighbour))
    
    return edges


# Adding edges
addEdge(graph, 'a', 'c')
addEdge(graph, 'b', 'c')
addEdge(graph, 'b', 'e')
addEdge(graph, 'c', 'd')
addEdge(graph, 'c', 'e')
addEdge(graph, 'c', 'a')
addEdge(graph, 'c', 'b')
addEdge(graph, 'e', 'b')
addEdge(graph, 'd', 'c')
addEdge(graph, 'e', 'c')

# Printing the graph insertion
print("After Insertion:")
traverseGraph(graph)
print()

# Removing an edge
removeEdge(graph, 'c', 'e')
print("\nAfter removing edge c -> e:")
traverseGraph(graph)
print()

print("Graph Traversal:")
traverseGraph(graph)
