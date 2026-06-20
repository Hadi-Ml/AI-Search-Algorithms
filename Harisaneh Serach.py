import time


def Harisaneh_Search(Problem_Graph, Problem_Hioristic, Initial_State, Goal_State):

    Frontier = [(Problem_Hioristic[Initial_State], Initial_State)]

    Explored = set()

    Parent = dict()

    Solution = []

    while True:

        Frontier.sort(reverse=True)

        if not Frontier:

            return "Failure"

        Node = Frontier.pop()[1]

        if Node == Goal_State:

            Solution.append(Goal_State)

            Child = Node

            while Child != Initial_State:

                Solution.append(Parent[Child])

                Child = Parent[Child]

            Solution.reverse()

            return (" -> ".join(Solution))

        Explored.add(Node)

        for Child in Problem_Graph[Node]:

            if (Child not in Explored) and (Child not in Frontier):

                Frontier.append((Problem_Hioristic[Child], Child))

                Parent[Child] = Node


if __name__ == "__main__":

    Problem1_Graph = {
        'Arad': ['Timisoara', 'Sibiu', 'Zerind'],
        'Timisoara': ['Arad', 'Lugoj'],
        'Lugoj': ['Timisoara', 'Mehadia'],
        'Mehadia': ['Lugoj', 'Dobreta'],
        'Dobreta': ['Mehadia', 'Craiova'],
        'Craiova': ['Dobreta', 'Rimnicu Vilcea','Pitesti'],
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

    Problem1_Hioristic = {
        'Arad': 366,
        'Bucharest': 0,
        'Craiova': 160,
        'Dobreta': 242,
        'Eforie': 161,
        'Fagaras': 178,
        'Giurgiu': 77,
        'Hirsova': 151,
        'Iasi': 226,
        'Lugoj': 244,
        'Mehadia': 241,
        'Neamt': 234,
        'Oradea': 380,
        'Pitesti': 98,
        'Rimnicu Vilcea': 193,
        'Sibiu': 253,
        'Timisoara': 329,
        'Urziceni': 80,
        'Vaslui': 199,
        'Zerind': 374
    }

    Problem2_Graph = {
        'S': ['A', 'D'],
        'A': ['B', 'G'],
        'D': ['B', 'E'],
        'B': ['C'],
        'C': ['G'],
        'E': ['G'],
        'G': []
    }

    Problem2_Hioristic = {
        'S': 7,
        'A': 9,
        'D': 5,
        'B': 4,
        'C': 2,
        'E': 3,
        'G': 0
    }

    Start = time.perf_counter()

    # Path = Harisaneh_Search(Problem_Graph=Problem1_Graph, Problem_Hioristic=Problem1_Hioristic, Initial_State='Arad', Goal_State='Bucharest')

    Path = Harisaneh_Search(Problem_Graph=Problem2_Graph, Problem_Hioristic=Problem2_Hioristic, Initial_State='S', Goal_State='G')

    End = time.perf_counter()

    print(f"\nPath of this Problem is {Path} , Executed in {(End - Start) * 1000:.4f} ms")
