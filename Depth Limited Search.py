import time

CutOff = "cutoff"

global Parent

global Solution

Parent = {}

Solution = []

def Depth_Limited_Search (Problem, Limit, Initial_State, Goal_State):

    Parent.clear()

    Solution.clear()

    Parent[Initial_State] = None

    return Recursive_DLS(Initial_State, Problem, Limit, Goal_State)


def Recursive_DLS (Node, Problem, Limit, Goal_State):

    if Node == Goal_State:

        Solution.append(Goal_State)

        Child = Goal_State

        while Parent[Child] is not None:

            Solution.append(Parent[Child])

            Child = Parent[Child]

        Solution.reverse()

        return " -> ".join(Solution)

    elif Limit == 0:

        return CutOff

    else:

        Cut_Off_Occured = False

        for Child in Problem[Node]:

            Parent[Child] = Node

            result = Recursive_DLS(Child, Problem, Limit - 1, Goal_State)

            if result == CutOff :

                Cut_Off_Occured = True

            elif result is not None:

                return result

        if Cut_Off_Occured:

            return  CutOff




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

    for Limit in range (1, 6):

        # Path = Depth_Limited_Search(Problem=Problem1, Limit=Limit, Initial_State='A', Goal_State='O')

        Path = Depth_Limited_Search(Problem=Problem2, Limit=Limit, Initial_State='S', Goal_State='G')

        End = time.perf_counter()

        print(f"\nPath of this Problem is {Path} with L = {Limit}, Executed in {(End - Start)*1000:.4f} ms")