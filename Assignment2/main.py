"""
Homework 2
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.02.02
"""
import random


def eulerian_cycle(graph, random_start=True, choice_start=0):
    """
    generates a string which denotes a Eulerian cycle within the graph
    :param graph: the graph on which this function will find a eulerian cycle
    :param random_start: if set to True, overrides choice_start with a random vertex
    :param choice_start: choose which vertex in the graph to start with
    """
    if len(graph) == 0 or len(graph) == 1:
        return ""

    stack, vertices, visited_edges = [], [], []

    # deciding where to start by generating a random start location, if random_start is set to True;
    # at the same time, check if there are any vertices which lead no where; if so, then it is impossible to create
    # a eulerian cycle
    for vertex in graph:
        vertices.append(vertex)
        if not graph[vertex]:
            return "Eulerian cycle impossible"
    if random_start:
        stack.append(vertices[random.randint(0, len(graph)-1)])
    else:
        stack.append(vertices[choice_start])

    path = ""  # the string which will eventually have the entire path
    while len(stack) != 0:
        ptr = stack[-1]
        # generate a list of unvisited paths
        unvisited_paths = []
        for next_vertex in graph[ptr]:
            if (ptr, next_vertex) not in visited_edges:
                unvisited_paths.append((ptr, next_vertex))

        if len(unvisited_paths) == 0:  # if no unvisited edges
            stack = stack[:-1]
            path += str(ptr) + ">-"
        else:  # if ptr -> current_edge is unvisited, go to one vertex
            stack.append(unvisited_paths[0][1])  # appending a vertex
            visited_edges.append(unvisited_paths[0])  # appending a path

    # return the path by reversing the string and shaving off the first two characters (which were "->")
    return path[::-1][2:]


'''TEST CASES'''
def test_eulerian_cycle_positive():
    """positive test case with rosalind data"""
    rosalind_graph = {
         0: [3],
         1: [0],
         2: [1, 6],
         3: [2],
         4: [2],
         5: [4],
         6: [5, 8],
         7: [9],
         8: [7],
         9: [6]
    }
    output = eulerian_cycle(rosalind_graph, random_start=False, choice_start=6)
    print("Testing on the rosalind dataset")
    print("Input: " + str(rosalind_graph))
    print("Should Be: \"6->5->4->2->1->0->3->2->6->8->7->9->6\"")
    print("Output: \"" + output + "\"")
    print("Test Passed: " + str("6->5->4->2->1->0->3->2->6->8->7->9->6" == output))
    print()


def test_eulerian_cycle_negative():
    """negative test case"""
    graph = {
        0: [1],
        1: 0
    }
    output = eulerian_cycle(graph, random_start=False)
    print("Testing on a graph with no Eulerian cycle")
    print("Input: " + str(graph))
    print("Should Be: \"Eulerian cycle impossible\"")
    print("Output: \"" + output + "\"")
    print("Test Passed: " + str("Eulerian cycle impossible" == output))
    print()


def test_eulerian_cycle_empty():
    graph = {}
    output = eulerian_cycle(graph, random_start=False)
    print("Testing on a graph with no Eulerian cycle")
    print("Input: " + str(graph))
    print("Should Be: \"\"")
    print("Output: \"" + output + "\"")
    print("Test Passed: " + str("" == output))
    print()


if __name__ == '__main__':
    test_eulerian_cycle_positive()
    test_eulerian_cycle_negative()
    test_eulerian_cycle_empty()
