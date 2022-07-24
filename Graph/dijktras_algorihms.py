# Finds the shortest path between two vertices on a graph
# using Priority queue to find the next node with min short distance to traverse its neighbours

import math as m

# ---- Priority Queue without binary heap (Complexity: O(N*logN))


class Priority_Queue:
    def __init__(self) -> None:
        self.values = []

    def __repr__(self) -> str:
        return f"{self.values}"

    def sort(self):
        self.values = sorted(self.values, key=lambda v: v["priority"])

    def enqueue(self, value, priority):
        self.values.append({"node": value, "priority": priority})
        self.sort()

    def dequeue(self):
        popped = self.values.pop(0)
        return popped


class Weighted_Graph:
    def __init__(self) -> None:
        self.adjacency_list = {}

    def __repr__(self) -> None:
        return f"{self.adjacency_list}"

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_list[vertex1].append(
            {"node": vertex2, "weight": weight})

        self.adjacency_list[vertex2].append(
            {"node": vertex1, "weight": weight})

    def dijktra(self, start, finish):
        nodes = Priority_Queue()
        distances = {}
        previous = {}
        shortest_path = []
        smallest = None

        # building up initial states
        for vertex in self.adjacency_list.keys():
            if vertex == start:
                distances[vertex] = 0
                nodes.enqueue(vertex, 0)
            else:
                distances[vertex] = m.inf
                nodes.enqueue(vertex, m.inf)
            previous[vertex] = None

        # as long as there is something to visit
        while len(nodes.values):
            smallest = nodes.dequeue()["node"]

            if smallest == finish:
                # we are done
                # we need to build path to return
                while(previous[smallest]):
                    shortest_path.append(previous[smallest])
                    smallest = previous[smallest]
                break

            if smallest or distances[smallest] != m.inf:
                for neighbour in self.adjacency_list[smallest]:
                    # calculate new distance to neigbouring node
                    candidate = distances[smallest] + neighbour["weight"]
                    if candidate < distances[neighbour["node"]]:
                        # updating new smallest distance to neighbour
                        distances[neighbour["node"]] = candidate
                        # updating previous - How we got to neighbour
                        previous[neighbour["node"]] = smallest
                        # enqueue in the  priority queue with new priority
                        nodes.enqueue(neighbour["node"], candidate)
        shortest_path.insert(0, finish)
        shortest_path.reverse()
        return shortest_path


graph = Weighted_Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")

graph.add_edge("A", "B", 4)
graph.add_edge("A", "C", 2)
graph.add_edge("B", "E", 3)
graph.add_edge("C", "D", 2)
graph.add_edge("C", "F", 4)
graph.add_edge("D", "E", 3)
graph.add_edge("D", "F", 1)
graph.add_edge("E", "F", 1)

# print(graph)

print(graph.dijktra("A", "E"))
