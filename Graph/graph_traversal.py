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

    def depth_first_search_recursive(self, starting_node):
        result = []
        visited_vertices = {}

        def dfs(vertex):
            if not vertex:
                return None
            visited_vertices[vertex] = True
            result.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited_vertices.keys():
                    dfs(neighbor)
        dfs(starting_node)

        return result


g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")


g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")
print(g)
print(g.depth_first_search_recursive("A"))
