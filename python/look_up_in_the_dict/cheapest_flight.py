def create_graph(data: list) -> dict:
    graph = {}
    for trip in data:
        src, dst, price = trip
        if src not in graph:
            graph[src] = {}
        if dst not in graph:
            graph[dst] = {}
        graph[src][dst] = price
        
    return graph

def cheapest_flight(costs: list, first: str, final: str) -> int:
    flights_graph = create_graph(costs)
    print(flights_graph)
    if first not in flights_graph: 
        return None

    distances = {node: float('inf') for node in flights_graph}
    distances[first] = 0
    visited = set()
    while len(visited) < len(flights_graph):
        min_distance = float('inf')
        current_node = None

        for node in flights_graph:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node
        if current_node is None:
            break

        visited.add(current_node)

        for neighbor, price in flights_graph[current_node].items():
            if neighbor not in visited:
                new_distance = distances[current_node] + price
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances[final] if distances[final] != float('inf') else 0


print("Example:")
print(cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C"))

# These "asserts" are used for self-checking
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "A", "C") == 70
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["B", "C", 50]], "C", "A") == 70
)
assert (
    cheapest_flight(
        [
            ["A", "C", 40],
            ["A", "B", 20],
            ["A", "D", 20],
            ["B", "C", 50],
            ["D", "C", 70],
        ],
        "D",
        "C",
    )
    == 60
)
assert (
    cheapest_flight([["A", "C", 100], ["A", "B", 20], ["D", "F", 900]], "A", "F") == 0
)
assert (
    cheapest_flight(
        [["A", "B", 10], ["A", "C", 15], ["B", "D", 15], ["C", "D", 10]], "A", "D"
    )
    == 25
)

print("The mission is done! Click 'Check Solution' to earn rewards!")
