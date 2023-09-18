import heapq

class PuzzleNode:
    def __init__(self, state, parent, action, cost):
        self.state = state          # Current state of the puzzle
        self.parent = parent        # Parent node
        self.action = action        # Action (move) taken to reach this state
        self.cost = cost            # Cost (usually the number of moves)
    
    def __lt__(self, other):
        # Comparison function for priority queue
        return self.cost < other.cost

def get_blank_position(state):
    # Find the position of the blank space (0) in the puzzle
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal_state(state, goal_state):
    # Check if the current state matches the goal state
    return state == goal_state

def get_neighbors(state):
    # Generate neighboring states by sliding tiles
    neighbors = []
    blank_i, blank_j = get_blank_position(state)

    # Possible moves: up, down, left, right
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for move in moves:
        new_i, new_j = blank_i + move[0], blank_j + move[1]

        if 0 <= new_i < 3 and 0 <= new_j < 3:
            # Create a new state by swapping the blank space with the adjacent tile
            new_state = [list(row) for row in state]
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            neighbors.append(new_state)

    return neighbors

def calculate_heuristic(state, goal_state):
    # Calculate the Manhattan distance heuristic
    h = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_i, goal_j = divmod(tile - 1, 3)
                h += abs(i - goal_i) + abs(j - goal_j)
    return h

def solve_puzzle(initial_state, goal_state):
    open_set = []        # Priority queue for open nodes
    closed_set = set()   # Set of closed nodes (already explored)

    # Initialize the open set with the initial state
    initial_node = PuzzleNode(initial_state, None, None, 0)
    heapq.heappush(open_set, initial_node)

    while open_set:
        # Pop the node with the lowest cost from the open set
        current_node = heapq.heappop(open_set)

        if is_goal_state(current_node.state, goal_state):
            # Found the goal state
            return reconstruct_path(current_node)

        closed_set.add(tuple(map(tuple, current_node.state)))  # Add the current state to the closed set

        for neighbor_state in get_neighbors(current_node.state):
            if tuple(map(tuple, neighbor_state)) not in closed_set:
                # Calculate the cost of the neighbor node (number of moves)
                neighbor_node = PuzzleNode(neighbor_state, current_node, None, current_node.cost + 1)
                neighbor_node.cost += calculate_heuristic(neighbor_state, goal_state)

                # Check if the neighbor node is already in the open set
                in_open_set = any(neighbor_node.state == node.state for node in open_set)

                if not in_open_set:
                    heapq.heappush(open_set, neighbor_node)

    return None  # No solution found

def reconstruct_path(node):
    # Reconstruct and return the path from the initial state to the goal state
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return path[::-1]

# Example usage:
initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

solution_path = solve_puzzle(initial_state, goal_state)

if solution_path:
    for step, state in enumerate(solution_path):
        print(f"Step {step + 1}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
