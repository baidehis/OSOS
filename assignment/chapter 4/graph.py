# Initialise vertices and edge of ABCDE

graph = {
    "A":["B","C"]
    "B":["A","D"]
    "C":["A","D","E"]
    "D":["C","B"]
    "E":["C"]
     }

for vertex in graph:
    print(vertex, "-> ", )
    print()
    #Function to print connected vertices
    def print_connected_vertices(graph, vertex):
    if vertex is not in graph:
        print("vertex not in graph!")
        return

        print