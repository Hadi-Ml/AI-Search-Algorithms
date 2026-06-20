from collections import deque
import time


def Breadth_First_Search (Problem, Initial_State, Goal_State):

    if Initial_State == Goal_State:

        return Initial_State

    Frontier = deque([Initial_State])

    Explored = set()

    Parent = dict()

    Solution = []

    while True:
        
        if not Frontier:

            return "Failure"

        Node = Frontier.popleft()

        Explored.add(Node)

        for Child in Problem[Node]:

            if (Child not in Explored) and (Child not in Frontier):
                
                if Child == Goal_State:

                    Parent[Child] = Node

                    Solution.append(Goal_State)

                    while Child != Initial_State:
                            
                            Solution.append(Parent[Child])

                            Child = Parent[Child]
                        
                    Solution.reverse()

                    return " -> ".join(Solution)
                
                else:

                    Frontier.append(Child)

                    Parent[Child] = Node





if __name__ == "__main__" :

    Problem1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
    }

    Problem2 = {
    'Arad': ['Timisoara', 'Sibiu', 'Zerind'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Rimnicu Vilcea', 'Fagaras'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
    }

    Problem3 = {
    'S': ['A', 'D'],
    'A': ['B'],
    'B': ['C', 'G'],
    'C': ['G'],
    'D': ['G'],
    'G': []
    }

    Start = time.perf_counter()

    # Path = Breadth_First_Search(Problem=Problem1, Initial_State='A', Goal_State='G')

    # Path = Breadth_First_Search(Problem=Problem2, Initial_State='Arad', Goal_State='Bucharest')

    Path = Breadth_First_Search(Problem=Problem3, Initial_State='S', Goal_State='G')

    End = time.perf_counter()


    print(f"\nPath of this Problem is {Path} , Executed in {(End - Start)*1000:.4f} ms\n")