from collections import deque
from itertools import count
import time


class Searching_Algorithms():

    def __init__(self):
        self.CutOff = "cutoff"
        self.Parent = {}
        self.Solution = []
        self.Depth = {}
        self.Visited = set()

    def Breadth_First_Search(self, Problem, Initial_State, Goal_State):
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

    def Uniform_Cost_Search(self, Problem, Initial_State, Goal_State):
        Frontier = [(0, Initial_State)]
        Explored = set()
        Parent = dict()
        Solution = []
        Frontier_Nodes = [Initial_State]
        while True:
            Frontier.sort(reverse=True)
            if not Frontier:
                return "Failure"
            Node_Cost, Node = Frontier.pop()
            if Node == Goal_State:
                Solution.append(Goal_State)
                Child = Node
                while Child != Initial_State:
                    Solution.append(Parent[Child])
                    Child = Parent[Child]
                Solution.reverse()
                return (" -> ".join(Solution), Node_Cost)
            Explored.add(Node)
            for Child, Child_Cost in Problem[Node]:
                if (Child not in Explored) and (Child not in Frontier_Nodes):
                    Frontier.append((Child_Cost + Node_Cost, Child))
                    Frontier_Nodes.append(Child)
                    Parent[Child] = Node
                elif Child in Frontier_Nodes:
                    for Index, CostNode in enumerate(Frontier):
                        if CostNode[1] == Child:
                            if CostNode[0] > Child_Cost + Node_Cost:
                                Frontier.pop(Index)
                                Frontier.append((Child_Cost + Node_Cost, Child))
                                Frontier.sort(reverse=True)
                                Parent.pop(Child)
                                Parent[Child] = Node

    def Depth_First_Search(self, Problem, Initial_State, Goal_State):
        self.Parent.clear()
        self.Solution.clear()
        self.Visited.clear()
        self.Parent[Initial_State] = None
        return self.Recursive_DLS1(Initial_State, Problem, Goal_State)

    def Recursive_DLS1(self, Node, Problem, Goal_State):
        if Node in self.Visited:
            return None
        self.Visited.add(Node)

        if Node == Goal_State:
            self.Solution.append(Goal_State)
            Child = Goal_State
            while self.Parent[Child] is not None:
                self.Solution.append(self.Parent[Child])
                Child = self.Parent[Child]
            self.Solution.reverse()
            return " -> ".join(self.Solution)
        else:
            for Child in Problem[Node]:
                if Child not in self.Visited:
                    self.Parent[Child] = Node
                    result = self.Recursive_DLS1(Child, Problem, Goal_State)
                    if result is not None:
                        return result
            return None

    # def Depth_Limited_Search(self, Problem, Limit, Initial_State, Goal_State):
    #     self.Parent.clear()
    #     self.Solution.clear()
    #     self.Parent[Initial_State] = None
    #     return self.Recursive_DLS2(Initial_State, Problem, Limit, Goal_State)
    #
    # def Recursive_DLS2(self, Node, Problem, Limit, Goal_State):
    #     if Node == Goal_State:
    #         current = Node
    #         while current is not None:
    #             self.Solution.append(current)
    #             current = self.Parent.get(current)
    #         self.Solution.reverse()
    #         return " -> ".join(self.Solution)
    #     elif Limit == 0:
    #         return self.CutOff
    #     else:
    #         Cut_Off_Occured = False
    #         for Child in Problem[Node]:
    #             self.Parent[Child] = Node
    #             result = self.Recursive_DLS2(Child, Problem, Limit - 1, Goal_State)
    #             if result == self.CutOff:
    #                 Cut_Off_Occured = True
    #             elif result is not None:
    #                 return result
    #         if Cut_Off_Occured:
    #             return self.CutOff
    #         return None

    def Iterative_Deepening_Search(self, Problem, Initial_State, Goal_State):
        from itertools import count
        for Limit in count(0):
            self.Parent.clear()
            self.Depth.clear()
            self.Solution.clear()
            self.Parent[Initial_State] = None
            self.Depth[Initial_State] = 0
            result = self.Depth_Limited_Search_Iterative(Problem, Limit, Initial_State, Goal_State)
            if result != self.CutOff and result is not None:
                return result, Limit
        return None, None

    def Depth_Limited_Search_Iterative(self, Problem, Limit, Initial_State, Goal_State):
        Frontier = deque([Initial_State])
        self.Parent.clear()
        self.Depth.clear()
        self.Parent[Initial_State] = None
        self.Depth[Initial_State] = 0

        while Frontier:
            Node = Frontier.pop()
            if Node == Goal_State:
                self.Solution.clear()
                self.Solution.append(Goal_State)
                Child = Goal_State
                while self.Parent[Child] is not None:
                    self.Solution.append(self.Parent[Child])
                    Child = self.Parent[Child]
                self.Solution.reverse()
                return " -> ".join(self.Solution)

            if self.Depth[Node] < Limit:
                for Child in Problem[Node]:
                    if Child not in self.Parent:
                        Frontier.append(Child)
                        self.Parent[Child] = Node
                        self.Depth[Child] = self.Depth[Node] + 1

        return self.CutOff


    def Harisaneh_Search(self, Problem_Graph, Problem_Hioristic, Initial_State, Goal_State):
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


    def A_Start_Search(self, Problem_Graph, Problem_Hioristic, Initial_State, Goal_State):

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


if "__main__" == __name__:

    Problem_Graph = {
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

    Problem_with_Cost = {
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

    Problem_Hioristic = {
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


    Object = Searching_Algorithms()

    Start = time.perf_counter()

    Path = Object.Breadth_First_Search(Problem=Problem_Graph, Initial_State='Arad', Goal_State='Bucharest')

    End = time.perf_counter()

    print(f"\nPath of this Problem with Breadth First Search is {Path} , Executed in {(End - Start) * 1000:.4f} ms")


    Start = time.perf_counter()

    Path = Object.Uniform_Cost_Search(Problem=Problem_with_Cost, Initial_State='Arad', Goal_State='Bucharest')

    End = time.perf_counter()

    print(f"\nPath of this Problem with Uniform Cost Search is {Path} , Executed in {(End - Start) * 1000:.4f} ms")


    Start = time.perf_counter()

    Path = Object.Depth_First_Search(Problem=Problem_Graph, Initial_State='Arad', Goal_State='Bucharest')

    End = time.perf_counter()

    print(f"\nPath of this Problem with Depth First Search is {Path} , Executed in {(End - Start) * 1000:.4f} ms")


    # Start = time.perf_counter()
    #
    # Path = Object.Depth_Limited_Search(Problem=Problem_Graph, Limit=5, Initial_State='Arad', Goal_State='Bucharest')
    #
    # End = time.perf_counter()
    #
    # print(f"\nPath of this Problem with Depth Limited Search is {Path} , Executed in {(End - Start) * 1000:.4f} ms")


    Start = time.perf_counter()

    Path = Object.Iterative_Deepening_Search(Problem=Problem_Graph, Initial_State='Arad', Goal_State='Bucharest')

    End = time.perf_counter()

    print(f"\nPath of this Problem with Iterative Deepening Search is {Path} , Executed in {(End - Start) * 1000:.4f} ms")


    Start = time.perf_counter()

    Path = Object.Harisaneh_Search(Problem_Graph=Problem_Graph, Problem_Hioristic=Problem_Hioristic, Initial_State='Arad', Goal_State='Bucharest')

    End = time.perf_counter()

    print(f"\nPath of this Problem with Harisaneh Search is {Path} , Executed in {(End - Start) * 1000:.4f} ms")


    Start = time.perf_counter()

    Path = Object.A_Start_Search(Problem_Graph=Problem_with_Cost, Problem_Hioristic=Problem_Hioristic, Initial_State='Arad', Goal_State='Bucharest')

    End = time.perf_counter()

    print(f"\nPath of this Problem with A* Search is {Path} , Executed in {(End - Start) * 1000:.4f} ms\n")



