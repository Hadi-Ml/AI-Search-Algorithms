import time
from collections import deque
from itertools import count

CutOff = "cutoff"

global Parent, Depth, Solution

Parent = {}

Depth = {}

Solution = []

def Iterative_Deepening_Search (Problem, Initial_State, Goal_State):

    for Limit in count(0):

        Parent.clear()

        Depth.clear()

        Solution.clear()

        Parent[Initial_State] = None

        Depth[Initial_State] = 0

        result = Depth_Limited_Search(Initial_State, Problem, Limit, Goal_State)

        if result != CutOff:

            Solution.append(Goal_State)

            Child = Goal_State

            while Parent[Child] is not None:

                Solution.append(Parent[Child])

                Child = Parent[Child]

            Solution.reverse()

            return " -> ".join(Solution), Limit



def Depth_Limited_Search (Initial_State, Problem, Limit, Goal_State):

    Frontier = deque([Initial_State])

    while Frontier:

        Node = Frontier.pop()

        if Node == Goal_State:

            return Node

        if Depth[Node] >= Limit:

            if Frontier:

                for node in Frontier:

                    if (Depth[node] < Depth[Node]) and node != Node:

                        Node = node

            else:

                result = CutOff

                return result

        else:

            for Child in Problem[Node]:

                Frontier.append(Child)

                Parent[Child] = Node

                Depth[Child] = Depth[Node] + 1




if "__main__" == __name__:

    Problem1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
    }

    Problem2 = {
    'S': ['A', 'D'],
    'A': ['B'],
    'B': ['C', 'G'],
    'C': ['G'],
    'D': ['G'],
    'G': []
    }

    Start = time.perf_counter()

    # Path, Limit =Iterative_Deepening_Search(Problem=Problem1, Initial_State='A', Goal_State='O')

    Path, Limit = Iterative_Deepening_Search(Problem=Problem2, Initial_State='S', Goal_State='G')

    End = time.perf_counter()

    print(f"\nPath of this Problem is {Path} with  the Minimum Limit = {Limit}, Executed in {(End - Start)*1000:.4f} ms")
