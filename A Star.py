import time


def A_Start_Search(Problem_Graph, Problem_Hioristic, Initial_State, Goal_State):

    Distance_Traveled = 0

    Frontier = [(Problem_Hioristic[Initial_State] + Distance_Traveled, Initial_State)]

    Explored = set()

    Parent = dict()

    Solution = []

    Frontier_Nodes = [Initial_State]

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

        for Child, Distance_Traveled in Problem_Graph[Node]:

            if (Child not in Explored) and (Child not in Frontier_Nodes):

                Copy_Node = Node

                Cost = 0

                while Copy_Node != Initial_State:

                    for Key in Problem_Graph:

                        if Parent[Copy_Node] == Key:

                            for Part in Problem_Graph[Key]:

                                if Part[0] == Copy_Node:

                                    Cost = Cost + Part[1]

                                    Copy_Node = Parent[Copy_Node]

                                    break

                            break



                Frontier.append((Problem_Hioristic[Child] + Distance_Traveled + Cost, Child))

                Frontier_Nodes.append(Child)

                Parent[Child] = Node

            elif Child in Frontier_Nodes:

                Copy_Node = Node

                Cost = 0

                while Copy_Node != Initial_State:

                    for Key in Problem_Graph:

                        if Parent[Copy_Node] == Key:

                            for Part in Problem_Graph[Key]:

                                if Part[0] == Copy_Node:

                                    Cost = Cost + Part[1]

                                    Copy_Node = Parent[Copy_Node]

                                    break

                            break

                for Index, CostNode in enumerate(Frontier):

                     if CostNode[1] == Child:

                        if CostNode[0] > Problem_Hioristic[Child] + Distance_Traveled + Cost:

                            Frontier.pop(Index)

                            Frontier.append((Problem_Hioristic[Child] + Distance_Traveled + Cost, Child))

                            Frontier.sort(reverse=True)

                            Parent.pop(Child)

                            Parent[Child] = Node



if __name__ == "__main__":

    Problem1_Graph = {
    'Arad': [('Timisoara', 118), ('Sibiu', 140), ('Zerind', 75)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Rimnicu Vilcea', 80), ('Fagaras', 99)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
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
        'S': [('A', 3), ('D', 2)],
        'A': [('S', 3), ('B', 5), ('G', 10)],
        'D': [('S', 2), ('B', 1), ('E', 4)],
        'B': [('A', 5), ('D', 1), ('E', 1), ('C', 2)],
        'C': [('B', 2), ('G', 4)],
        'E': [('D', 4), ('B', 1), ('G', 3)],
        'G': [('A', 10), ('C', 4), ('E', 3)]
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

    # Path = A_Start_Search(Problem_Graph=Problem1_Graph, Problem_Hioristic=Problem1_Hioristic, Initial_State='Arad', Goal_State='Bucharest')

    Path = A_Start_Search(Problem_Graph=Problem2_Graph, Problem_Hioristic=Problem2_Hioristic, Initial_State='S', Goal_State='G')

    End = time.perf_counter()

    print(f"\nPath of this Problem is {Path} , Executed in {(End - Start) * 1000:.4f} ms")
