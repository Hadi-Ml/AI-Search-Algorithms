import time

global Parent

global Solution

Parent = {}

Solution = []

def Depth_First_Search (Problem, Initial_State, Goal_State):

    Parent.clear()

    Solution.clear()

    Parent[Initial_State] = None

    return Recursive_DLS(Initial_State, Problem, Goal_State)


def Recursive_DLS (Node, Problem, Goal_State):

    if Node == Goal_State:

        Solution.append(Goal_State)

        Child = Goal_State

        while Parent[Child] is not None:

            Solution.append(Parent[Child])

            Child = Parent[Child]

        Solution.reverse()

        return " -> ".join(Solution)

    else:

        for Child in Problem[Node]:

            Parent[Child] = Node

            result = Recursive_DLS(Child, Problem, Goal_State)

            if result is not None:

                return result




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

    Start = time.perf_counter()

    Path = Depth_First_Search(Problem=Problem1, Initial_State='A', Goal_State='O')

    End = time.perf_counter()


    print(f"\nPath of this Problem is {Path} , Executed in {(End - Start)*1000:.4f} ms")