class Graph:
   def __init__(self):
      self.adj={}

   def add_node(self, node):
      if node not in self.adj:
         self.adj[node]=[]
         print("Node added!\n")

   def delete_node(self, node):
      if node in self.adj:
         for i in self.adj:
            if node in self.adj[i]:
               self.adj[i].remove(node)
         del self.adj[node]
         print("Node deleted!\n")

   def add_edge(self, n1, n2, cost):
      if n1 in self.adj and n2 in self.adj:
         self.adj[n1].append((n2, cost))
         self.adj[n2].append((n1, cost))
         print("Edge added!\n")

   def delete_edge(self,n1,n2):
      if n1 in self.adj and n2 in self.adj:
         if n2 in self.adj[n1]:
            self.adj[n1].remove(n2)
            self.adj[n2].remove(n1)
            print("Edge removed!\n")

   def display(self):
      print("\nAdjacency list : ")
      for i in self.adj:
         print(i, "->", self.adj[i])
      print()

def a_star(graph, heuristics, start, goal_node):
    frontier = [(heuristics[start], start, [start], 0)]
    explored = set()
    while frontier:
        frontier.sort()
        nodes_in_frontier = [item[1] for item in frontier]
        print("\nFrontier :", nodes_in_frontier)
        print("Explored :", explored)
        f_cost, curr_node, path, g_cost = frontier.pop(0)
        print("Expanding :", curr_node, "g =", g_cost, "f =", f_cost)
        if curr_node == goal:
            print("\nGoal found!")
            return path, g_cost
        if curr_node in explored:
            continue
        explored.add(curr_node)
        for neighbor, edge_cost in graph.adj.get(curr_node, []):
            if neighbor not in explored:
                new_g_cost = g_cost + edge_cost
                new_f_cost = new_g_cost + heuristics.get(neighbor, 0)
                frontier.append((new_f_cost, neighbor, path + [neighbor], new_g_cost))
    print("Goal not found!")

graph = Graph()
num_nodes = int(input("\nEnter number of nodes : "))
for i in range(num_nodes):
   n = input(f"Enter node{i+1} : ")
   graph.add_node(n)

num_edges = int(input("Enter number of edges : "))
for i in range(num_edges):
   n1 = input("Enter node1 : ")
   n2 = input("Enter node2 : ")
   cost = int(input("Enter cost : "))
   graph.add_edge(n1, n2, cost)

print("1. Add Node\n2. Delete Node\n3. Add Edge\n4. Delete Edge\n5. Display\n6. A* Search\n7. Exit\n")
while True:
   ch = int(input("Enter choice : "))
   if ch == 1:
      n = input("Enter node : ")
      graph.add_node(n)

   elif ch == 2:
      n = input("Enter node : ")
      graph.delete_node(n)

   elif ch == 3:
      n1 = input("Enter node1 : ")
      n2 = input("Enter node2 : ")
      cost = int(input("Enter cost : "))
      graph.add_edge(n1, n2, cost)

   elif ch == 4:
      n1 = input("Enter node1 : ")
      n2 = input("Enter node2 : ")
      graph.delete_edge(n1,n2)

   elif ch == 5:
      graph.display()

   elif ch == 6:
      heuristics = {}
      print("\nEnter heuristic values:")
      for node in graph.adj:
         heuristics[node] = int(input(f"h({node}) : "))

      start = input("\nEnter start node : ")
      goal = input("Enter goal node : ")

      path, cost = a_star(graph, heuristics, start, goal)
      print("\nA* search path : ", path);
      print("Cost : ",cost)
      print()

   elif ch == 7:
      print("Exiting..\n")
      break

   else:
      print("Invalid choice!")