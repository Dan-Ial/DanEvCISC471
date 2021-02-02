#Homework 2
#By: Evelyn Yach (20071956)& Daniel Oh (20063998)
#2021.02.02

''' pseudo code for finding a eulerian cycle in a graph
EulerianCycle(Graph)
    form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
    while there are unexplored edges in Graph
        select a node newStart in Cycle with still unexplored edges
        form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
        Cycle ← Cycle’
    return Cycle
'''

def eulerian_cycle(graph):
