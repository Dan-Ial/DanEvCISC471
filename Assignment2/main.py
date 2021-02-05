"""
Homework 2
By: Evelyn Yach (20071956) & Daniel Oh (20063998)
2021.02.02
"""
import random

##################
# EULERIAN CYCLE #
##################
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


'''TEST CASES FOR EULERIAN CYCLE'''
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


def eulerian_cycle_main():
    print("EULERIAN CYCLE TEST CASES\n")
    test_eulerian_cycle_positive()
    test_eulerian_cycle_negative()
    test_eulerian_cycle_empty()


###########
# CONTIGS #
###########
def contigs(input_data):
    """
    generates a list of contigs from a list of input kmers
    :param input_data: A list of kmer strings
    :return: List of contigs found from the kmers
    """
    # check if input_data is valid, input_data must be a list of strings
    if isinstance(input_data, list):
        for element in input_data:
            if not isinstance(element, str):
                return "Invalid input"
    else:
        return "Invalid input"


    if len(input_data) == 0:
        return []

    graph, contigs_list, to_remove_list = {}, [], []

    # set up the graph
    for kmer in input_data:
        if kmer[:len(kmer)-1] not in graph:
            graph[kmer[:len(kmer)-1]] = []
        graph[kmer[:len(kmer)-1]].append(kmer[1:])

    for vertex in graph:

        edges_into_vertex, edges_out_of_vertex = num_of_inputs(vertex, graph), num_of_outputs(vertex, graph)

        if edges_into_vertex != 1 or edges_out_of_vertex != 1:
            # if there are more than 1 vertices that come after our current vertex
            if edges_out_of_vertex > 0:

                for vertex_prime in graph[vertex]:  # going through each vertex that branches out
                    non_branching_path = vertex + vertex_prime[-1]

                    # while we're still on a straight path
                    while num_of_inputs(vertex_prime, graph) == 1 and num_of_outputs(vertex_prime, graph) == 1:
                        non_branching_path = non_branching_path + graph[vertex_prime][0][-1]
                        vertex_prime = graph[vertex_prime][0]

                    contigs_list.append(non_branching_path)  # append a new contig

    return contigs_list


def num_of_inputs(vertex, graph):
    """
    returns a count of the number of edges/inputs that are going into the vertex
    :param vertex: the vertex we are concerned about
    :param graph: the graph that :vertex: is within
    :return: the number of edges entering the vertex
    """
    count = 0
    # find every instance of vertex in the outputs of other vertices
    for i in graph:
        if vertex in graph[i]:
            count += 1

    return count


def num_of_outputs(vertex, graph):
    """
    returns a count of the number of edges/inputs that are leaving the vertex
    :param vertex: the vertex we are concerned about
    :param graph: the graph that :vertex: is within
    :return: the number of edges leaving the vertex
    """
    if vertex in graph:
        # simply count
        return len(graph[vertex])

    return 0


'''TEST CASES FOR CONTIGS'''
def test_contigs_positive():
    """positive test case with rosalind data"""
    rosalind_data = ['ATG', 'ATG', 'TGT', 'TGG', 'CAT', 'GGA', 'GAT', 'AGA']
    output = contigs(rosalind_data)
    print("Testing on the rosalind dataset")
    print("Input: " + str(rosalind_data))
    # note: the rosalind site dataset has the sample output in a different order, with the same elements
    print("Should Be: \"['ATG', 'ATG', 'TGT', 'TGGA', 'CAT', 'GAT', 'AGA']\"")
    print("Output: \"" + str(output) + "\"")
    print("Test Passed: " + str(['ATG', 'ATG', 'TGT', 'TGGA', 'CAT', 'GAT', 'AGA'] == output))
    print()


def test_contigs_negative():
    """negative test case"""
    input_data = 'Not A Valid List'
    output = contigs(input_data)
    print("Testing on an invalid input")
    print("Input: " + str(input_data))
    print("Should Be: \"Invalid input\"")
    print("Output: \"" + str(output) + "\"")
    print("Test Passed: " + str("Invalid input" == output))
    print()


def test_contigs_empty():
    """negative test case"""
    input_data = []
    output = contigs(input_data)
    print("Testing on an empty list")
    print("Input: " + str(input_data))
    print("Should Be: \"[]\"")
    print("Output: \"" + str(output) + "\"")
    print("Test Passed: " + str([] == output))
    print()


def contig_main():
    print("CONTIG TEST CASES\n")
    test_contigs_positive()
    test_contigs_negative()
    test_contigs_empty()


if __name__ == '__main__':
    eulerian_cycle_main()
    contig_main()