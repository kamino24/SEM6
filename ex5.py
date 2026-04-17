import random
import math

class WumpusWorld:
    def __init__(self, n):
        self.n = n
        self.game_over = False
        self.agent_pos = (0, 0)
        self.pits = set()
        self.wumpus = None
        self.gold = None
        self.occupied_cells = {(0, 0)}
        self.last_bump = False
        self.last_scream = False

    def in_bounds(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n

    def get_adjacent(self, x, y):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        return [(x+dx, y+dy) for dx, dy in directions if self.in_bounds(x+dx, y+dy)]

    def _validate_and_place(self, name):
        while True:
            try:
                line = input(f"Enter {name} position (x y): ").split()
                pos = (int(line[0]), int(line[1]))
                if not self.in_bounds(*pos):
                    print(f"Error: {pos} is out of bounds!")
                elif pos in self.occupied_cells:
                    print(f"Error: Cell {pos} is already occupied!")
                else:
                    self.occupied_cells.add(pos)
                    return pos
            except:
                print("Invalid input. Enter two integers (e.g., 1 2).")

    def display_grid(self, message=""):
        adj = self.get_adjacent(*self.agent_pos)
        status_lines = [
            "--- SENSES ---",
            f"Breeze:  {'YES' if any(p in adj for p in self.pits) else 'NO'}",
            f"Smell:   {'YES' if self.wumpus in adj else 'NO'}",
            f"Glitter: {'YES' if self.gold in adj else 'NO'}",
            f"Bump:    {'YES' if self.last_bump else 'NO'}",
            f"Scream:  {'YES' if self.last_scream else 'NO'}",
            "--------------",
            f"Action: {message}"
        ]

        print("\n" + "=" * 40)
        for y in range(self.n - 1, -1, -1):
            row_str = "| "
            for x in range(self.n):
                row_str += "A " if (x, y) == self.agent_pos else ". "
            row_str += "|"

            idx = (self.n - 1) - y
            status_text = status_lines[idx] if idx < len(status_lines) else ""
            print(f"{row_str:<{self.n*2 + 5}} | {status_text}")
        print("=" * 40)

        x, y = self.agent_pos
        print(f"CURRENT LOCATION: ({x}, {y})")

        possible = []
        if self.in_bounds(x, y + 1): possible.append("up")
        if self.in_bounds(x, y - 1): possible.append("down")
        if self.in_bounds(x - 1, y): possible.append("left")
        if self.in_bounds(x + 1, y): possible.append("right")

        print(f"POSSIBLE DIRECTIONS: {', '.join(possible)}")

    def move(self, direction):
        self.last_bump = False
        x, y = self.agent_pos
        move_map = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
        dx, dy = move_map.get(direction, (0, 0))
        nx, ny = x + dx, y + dy

        if not self.in_bounds(nx, ny):
            self.last_bump = True
            # Updated message here
            self.display_grid("BUMPED THE WALL!")
            return

        self.agent_pos = (nx, ny)
        if self.agent_pos in self.pits:
            self.display_grid("FELL IN PIT!")
            print("GAME OVER.")
            self.game_over = True
        elif self.agent_pos == self.wumpus:
            self.last_scream = True
            self.display_grid("EATEN BY WUMPUS!")
            print("SCREAM! GAME OVER.")
            self.game_over = True
        elif self.agent_pos == self.gold:
            self.display_grid("GOLD FOUND!")
            print("Hurray VICTORY! \nYou have acquired the gold!")
            self.game_over = True
        else:
            self.display_grid(f"Moved {direction}")

def play():
    try:
        n_input = input("Enter grid size N: ")
        n = int(n_input) if n_input.isdigit() else 4
        game = WumpusWorld(n)

        print("\n1. Random Placement\n2. Manual Placement")
        choice = input("Choice: ")

        if choice == '1':
            cells = [(x, y) for x in range(n) for y in range(n) if (x,y) != (0,0)]
            random.shuffle(cells)
            game.wumpus = cells.pop()
            game.gold = cells.pop()
            for _ in range(math.floor(0.2 * (n*n))):
                if cells: game.pits.add(cells.pop())
        else:
            game.wumpus = game._validate_and_place("Wumpus")
            game.gold = game._validate_and_place("Gold")
            p_input = input("How many pits? ")
            num_pits = int(p_input) if p_input.isdigit() else 0
            for i in range(num_pits):
                game.pits.add(game._validate_and_place(f"Pit {i+1}"))

        game.display_grid("Game Started")
        while not game.game_over:
            action = input("\nMove (up/down/left/right): ").lower()
            if action in ["up", "down", "left", "right"]:
                game.move(action)
            else:
                print("Invalid command.")
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    play()
