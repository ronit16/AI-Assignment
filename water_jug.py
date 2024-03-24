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

def can_measure_water(m, n, d):
    if d > m + n:
        return -1

    visited = set()
    initial_state = (0, 0)
    
    # Using QueueFrontier for BFS
    frontier = QueueFrontier()
    frontier.add(Node(initial_state))

    while not frontier.empty():
        current_node = frontier.remove()
        jug1, jug2 = current_node.state

        if jug1 == d or jug2 == d:
            return current_node

        if current_node.state in visited:
            continue

        visited.add(current_node.state)

        # Fill jug 1
        frontier.add(Node((m, jug2), current_node, "Fill jug 1"))

        # Fill jug 2
        frontier.add(Node((jug1, n), current_node, "Fill jug 2"))

        # Empty jug 1
        frontier.add(Node((0, jug2), current_node, "Empty jug 1"))

        # Empty jug 2
        frontier.add(Node((jug1, 0), current_node, "Empty jug 2"))

        # Pour water from jug 1 to jug 2
        pour = min(jug1, n - jug2)
        frontier.add(Node((jug1 - pour, jug2 + pour), current_node, f"Pour {pour} units from jug 1 to jug 2"))

        # Pour water from jug 2 to jug 1
        pour = min(m - jug1, jug2)
        frontier.add(Node((jug1 + pour, jug2 - pour), current_node, f"Pour {pour} units from jug 2 to jug 1"))

    return None

def print_solution(solution_node):
    if solution_node is not None:
        steps = []
        actions = []
        while solution_node.parent is not None:
            steps.append(solution_node.state)
            actions.append(solution_node.action)
            solution_node = solution_node.parent

        steps.append(solution_node.state)
        
        print("Steps:")
        for step in steps[::-1]:
            print(step)

        print("\nActions:")
        for action in actions[::-1]:
            print(action)
        
        print("\nTotal Steps:", len(steps) - 1)
    else:
        print("It is not possible to measure the desired amount of water.")

m = 4
n = 3
d = 2

solution_node = can_measure_water(m, n, d)
print_solution(solution_node)