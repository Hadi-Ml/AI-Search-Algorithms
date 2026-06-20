import time


def Uniform_Cost_Search (Problem, Initial_State, Goal_State):

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

            while  Child != Initial_State:
                                
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





if __name__ == "__main__" :

    Problem1 = {
    'Sibiu': [('Rimnicu Vilcea', 80), ('Fagaras', 99)], 
    'Rimnicu Vilcea': [('Pitesti', 97)],
    'Fagaras': [('Bucharest', 211)],
    'Pitesti': [('Bucharest', 101)], 
    'Bucharest': [], 
    }

    Problem2 = {
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

    Start = time.perf_counter()

    # Path, Total_Cost = Uniform_Cost_Search(Problem=Problem1, Initial_State='Sibiu', Goal_State='Bucharest')

    Path, Total_Cost = Uniform_Cost_Search(Problem=Problem2, Initial_State='Arad', Goal_State='Bucharest')

    End = time.perf_counter()

    print(f"Path of this Problem is {Path} with Cost : {Total_Cost} km , Executed in {(End - Start)*1000:.4f} ms")
