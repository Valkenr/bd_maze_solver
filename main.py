from graphics import Window
from maze import Maze

def main():

    num_rows = 12
    num_cols = 16
    border = 50
    window_x = 800
    window_y = 600
    cell_size_x = (window_x - (2 * border)) / num_cols
    cell_size_y = (window_y - (2 * border)) / num_rows
    win = Window(window_x, window_y)

    maze = Maze(border, border,
                num_rows, num_cols,
                cell_size_x, cell_size_y,
                win, 69420)

    maze.solve()

    win.wait_for_close()


main()
