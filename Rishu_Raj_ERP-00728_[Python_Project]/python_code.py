
from collections import deque


maze = [
    ['P', '.', '.', '#', '#'],
    ['#', '#', '.', '#', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#'],
    ['#', '.', '.', '.', 'E']
]

ROWS = 5
COLS = 5

start = (0, 0)
exit_point = (4, 4)


directions = {
    'W': (-1, 0),
    'A': (0, -1),
    'S': (1, 0),
    'D': (0, 1)
}

def display_maze(player):

    print("\n--- MAZE ---")

    for r in range(ROWS):
        for c in range(COLS):

            if (r, c) == player:
                print('P', end=' ')

            else:
                print(maze[r][c], end=' ')

        print()

    print()



def play_game():

    player = start
    moves = 0

    print("\nUse W/A/S/D to move.")
    print("Reach E to escape the maze.")

    while player != exit_point:

        display_maze(player)

        key = input("Enter move (W/A/S/D): ").upper()

        
        if key not in directions:
            print("Invalid key! Use W, A, S or D only.")
            continue

        dr, dc = directions[key]

        new_row = player[0] + dr
        new_col = player[1] + dc

        
        if (new_row < 0 or new_row >= ROWS or
                new_col < 0 or new_col >= COLS):

            print("Cannot move outside the maze.")
            print("Player stays at", player)
            continue

        
        if maze[new_row][new_col] == '#':
            print("Wall ahead. Move blocked.")
            print("Player stays at", player)
            continue

        
        player = (new_row, new_col)
        moves += 1

        print("Player moved to", player)
        print("Moves:", moves)

    display_maze(player)

    print("\nCongratulations!")
    print("You escaped the maze!")
    print("Total moves:", moves)



def shortest_path():

    queue = deque([(start, 0)])

    visited = {start}

    while queue:

        (row, col), distance = queue.popleft()

        
        if (row, col) == exit_point:
            print("Shortest path length:", distance, "steps")
            return

        
        for dr, dc in directions.values():

            nr = row + dr
            nc = col + dc

            
            if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    maze[nr][nc] != '#' and
                    (nr, nc) not in visited):

                visited.add((nr, nc))

                queue.append(((nr, nc), distance + 1))

    print("No path found!")



while True:

    print("\n===== MAZE ESCAPE GAME =====")
    print("1. Play Game")
    print("2. Find Shortest Path")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        play_game()

    elif choice == '2':
        shortest_path()

    elif choice == '3':
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice!")
