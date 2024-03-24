import numpy as np

class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def add(self, node):
        self.queue.append(node)
        self.queue.sort(key=lambda x: x.cost)

    def remove(self):
        if self.empty():
            raise Exception("Empty Priority Queue")
        else:
            node = self.queue.pop(0)
            return node

    def empty(self):
        return len(self.queue) == 0

class Puzzle:
    def __init__(self, start, startIndex, goal, goalIndex):
        self.start = [start, startIndex]
        self.goal = [goal, goalIndex]
        self.solution = None

    def heuristic(self, state):
        # Manhattan distance heuristic
        start_positions = {state[0][i, j]: (i, j) for i in range(3) for j in range(3)}
        goal_positions = {self.goal[0][i, j]: (i, j) for i in range(3) for j in range(3)}

        total_distance = 0
        for num in range(1, 9):
            start_pos = start_positions[num]
            goal_pos = goal_positions[num]
            total_distance += abs(start_pos[0] - goal_pos[0]) + abs(start_pos[1] - goal_pos[1])

        return total_distance

    def neighbors(self, state):
        mat, (row, col) = state
        results = []

        if row > 0:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row - 1][col]
            mat1[row - 1][col] = 0
            results.append(('up', [mat1, (row - 1, col)]))
        if col > 0:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row][col - 1]
            mat1[row][col - 1] = 0
            results.append(('left', [mat1, (row, col - 1)]))
        if row < 2:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row + 1][col]
            mat1[row + 1][col] = 0
            results.append(('down', [mat1, (row + 1, col)]))
        if col < 2:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row][col + 1]
            mat1[row][col + 1] = 0
            results.append(('right', [mat1, (row, col + 1)]))

        return results

    def print_solution(self):
        solution = self.solution if self.solution is not None else None
        print("Start State:\n", self.start[0], "\n")
        print("Goal State:\n",  self.goal[0], "\n")
        print("\nStates Explored: ", self.num_explored, "\n")
        print("Solution:\n ")
        for action, cell in zip(solution[0], solution[1]):
            print("action: ", action, "\n", cell[0], "\n")
        print("Goal Reached!!")

    def does_not_contain_state(self, state):
        return tuple(map(tuple, state[0])) not in self.explored

    def solve(self):
        self.num_explored = 0

        start = Node(state=self.start, parent=None, action=None, cost=0)
        frontier = PriorityQueue()
        frontier.add(start)

        self.explored = set()

        while True:
            if frontier.empty():
                raise Exception("No solution")

            node = frontier.remove()
            self.num_explored += 1

            if (node.state[0] == self.goal[0]).all():
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            self.explored.add(tuple(map(tuple, node.state[0])))

            for action, state in self.neighbors(node.state):
                if state not in frontier.queue and self.does_not_contain_state(state):
                    child = Node(state=state, parent=node, action=action, cost=node.cost + 1 + self.heuristic(state))
                    frontier.add(child)



start = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])
goal = np.array([[2, 8, 1], [0, 4, 3], [7, 6, 5]])

startIndex = (1, 1)
goalIndex = (1, 0)

p = Puzzle(start, startIndex, goal, goalIndex)
p.solve()
p.print_solution()
