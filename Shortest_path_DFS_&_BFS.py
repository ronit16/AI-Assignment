class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any((node.state == state) for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier.pop()
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier.pop(0)
            return node

class Search:
    @staticmethod
    def dfs(graph, initial_state, goal_state):
        start_node = Node(state=initial_state)
        frontier = StackFrontier()
        frontier.add(start_node)
        explored = set()

        while not frontier.empty():
            current_node = frontier.remove()
            current_state = current_node.state

            if current_state == goal_state:
                return Search.path_to_goal(current_node)

            explored.add(current_state)

            for neighbor in graph.get(current_state, []):
                if neighbor not in explored and not frontier.contains_state(neighbor):
                    child_node = Node(state=neighbor, parent=current_node)
                    frontier.add(child_node)

        return None 

    @staticmethod
    def bfs(graph, initial_state, goal_state):
        start_node = Node(state=initial_state)
        frontier = QueueFrontier()
        frontier.add(start_node)
        explored = set()

        while not frontier.empty():
            current_node = frontier.remove()
            current_state = current_node.state

            if current_state == goal_state:
                return Search.path_to_goal(current_node)

            explored.add(current_state)

            for neighbor in graph.get(current_state, []):
                if neighbor not in explored and not frontier.contains_state(neighbor):
                    child_node = Node(state=neighbor, parent=current_node)
                    frontier.add(child_node)

        return None  

    @staticmethod
    def path_to_goal(node):
        path = []
        while node.parent is not None:
            path.append(node.state)
            node = node.parent
        path.append(node.state)
        return path[::-1]

def get_user_input():
    graph = {}
    edges = int(input("Enter the number of edges: "))
    for _ in range(edges):
        source, destination = input("Enter an edge (source destination): ").split()
        if source not in graph:
            graph[source] = []
        graph[source].append(destination)
    initial_state = input("Enter the initial state: ")
    goal_state = input("Enter the goal state: ")
    return graph, initial_state, goal_state

graph, initial_state, goal_state = get_user_input()

dfs_path = Search.dfs(graph, initial_state, goal_state)
bfs_path = Search.bfs(graph, initial_state, goal_state)

print("DFS Path:", dfs_path)
print("BFS Path:", bfs_path)
