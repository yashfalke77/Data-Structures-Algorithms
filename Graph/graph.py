# Undirected Graph

class Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def __repr__(self) -> str:
        return f"{self.adjacency_list}"

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
        if vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys():
            self.adjacency_list[vertex1] = [
                vertex for vertex in self.adjacency_list[vertex1] if vertex2 != vertex]
        if vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex2] = [
                vertex for vertex in self.adjacency_list[vertex2] if vertex1 != vertex]

    def remove_vertex(self, vertex):
        for _ in range(0, len(self.adjacency_list[vertex])):
            adjacent_vertex = self.adjacency_list[vertex].pop()
            self.remove_edge(vertex, adjacent_vertex)
        del self.adjacency_list[vertex]


g = Graph()
g.add_vertex("Dallas")
g.add_vertex("Tokyo")
g.add_vertex("Aspen")
g.add_vertex("Los Angeles")
g.add_vertex("Hong Kong")
g.add_edge("Dallas", "Tokyo")
g.add_edge("Dallas", "Aspen")
g.add_edge("Hong Kong", "Tokyo")
g.add_edge("Hong Kong", "Dallas")
g.add_edge("Los Angeles", "Hong Kong")
g.add_edge("Los Angeles", "Aspen")
print(g)
g.remove_vertex("Tokyo")
print(g)
