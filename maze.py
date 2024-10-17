import time
import random
from cell import Cell
from graphics import Point

class Maze:
    def __init__(
            self,
            x1, y1,
            num_rows, num_cols,
            cell_size_x, cell_size_y,
            win=None, seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)

        self._create_cells()


    def _create_cells(self):
        for i in range (self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited()

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(Point(x1, y1), Point(x2, y2), "black")
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        print(f"At: ({i}, {j}) of ({self._num_cols}, {self._num_rows})")
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                    to_visit.append("left")
            if j > 0 and not self._cells[i][j-1].visited:
                    to_visit.append("up")
            if i < self._num_cols-1 and not self._cells[i+1][j].visited:
                    to_visit.append("right")
            if j < self._num_rows-1 and not self._cells[i][j+1].visited:
                    to_visit.append("down")
            if to_visit == []:
                self._draw_cell(i, j)
                return
            print(f"to_visit: {to_visit}")
            direction = random.randrange(len(to_visit))
            print(f"Chosen Rand: to_visit[{direction}]={to_visit[direction]}")
            if to_visit[direction] == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._draw_cell(i, j)
                self._break_walls_r(i, j-1)
            if to_visit[direction] == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._draw_cell(i, j)
                self._break_walls_r(i, j+1)
            if to_visit[direction] == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._draw_cell(i, j)
                self._break_walls_r(i+1, j)
            if to_visit[direction] == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._draw_cell(i, j)
                self._break_walls_r(i-1, j)

    def _reset_visited(self):
        for i in range (self._num_cols):
            for j in range(self._num_rows):
                print(f"resetting visited on ({i}, {j})")
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        print(f"Solving at: ({i}, {j})")
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True

        if i > 0 and \
            not self._cells[i][j].has_left_wall and \
            not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], True)

        if i < self._num_cols-1 and \
            not self._cells[i][j].has_right_wall and \
            not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], True)

        if j < self._num_rows-1 and \
            not self._cells[i][j].has_bottom_wall and \
            not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], True)

        if j > 0 and \
            not self._cells[i][j].has_top_wall and \
            not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], True)

        return False

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

