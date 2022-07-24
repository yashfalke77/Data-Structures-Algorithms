class Weighted_Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def __repr__(self) -> str:
        return f"{self.adjacency_list}"

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_list[vertex1].append(
            {"node": vertex2, "weight": weight})
        self.adjacency_list[vertex2].append(
            {"node": vertex1, "weight": weight})

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys():
            self.adjacency_list[vertex1] = [
                vertex for vertex in self.adjacency_list[vertex1] if vertex["node"] != vertex2]
        if vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex2] = [
                vertex for vertex in self.adjacency_list[vertex2] if vertex["node"] != vertex1]

    def remove_vertex(self, vertex):
        for _ in range(0, len(self.adjacency_list[vertex])):
            adjacent_vertex = self.adjacency_list[vertex].pop()
            self.remove_edge(vertex, adjacent_vertex["node"])
        del self.adjacency_list[vertex]


wg = Weighted_Graph()
wg.add_vertex("A")
wg.add_vertex("B")
wg.add_vertex("C")
wg.add_edge("A", "B", 9)
wg.add_edge("A", "C", 5)
wg.remove_edge("A", "C")
wg.remove_vertex("B")
print(wg)
