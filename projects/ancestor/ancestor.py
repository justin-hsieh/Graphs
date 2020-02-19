from util import Stack, Queue

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        If both exist, and a connection from v1 to v2
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    # initialize Graph
    ancestor_graph = Graph()

    # loop through ancestors and add each set as vertices
    for ancestor_set in ancestors:
        # add first vertex, then second one
        ancestor_graph.add_vertex(ancestor_set[0])
        ancestor_graph.add_vertex(ancestor_set[1])
    # add edges
    for ancestor_set in ancestors:
        ancestor_graph.add_edge(ancestor_set[1], ancestor_set[0])

    # initiate stack
    stack = Stack()
    # Put the starting point in the stack
    stack.push([starting_node])
    # Make a set to keep track of nodes visited
    visited = set()
    # Track the longest path
    longest_path = [starting_node]
    # While the stack is not empty
    while stack.size() > 0:
        # Pop the first item
        path = stack.pop()
        vertex = path[-1]
        # If vertex has not been visited
        if vertex not in visited:
            # add the vertex to visited
            visited.add(vertex)
            # For each edge in the item
            for next_vert in ancestor_graph.get_neighbors(vertex):
                # Copy the path
                new_path = list(path)
                new_path.append(next_vert)
                # Add that edge to the stack
                stack.push(new_path)
                # compare the path lengths and update
                if len(new_path) > len(longest_path):
                    longest_path = new_path
                # path may be same size size but path has changed so check last element for change
                if len(new_path) == len(longest_path) and new_path[-1] != longest_path[-1]:
                    longest_path = new_path

    if longest_path[-1] == starting_node:
        return -1
    else:
        return longest_path[-1]