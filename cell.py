from graphics import Point, Line

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._win = win

    def draw(self, p1, p2, line_color):
        if self._win is None:
            return

        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y

        left_wall = Line(Point(self._x1, self._y1),Point(self._x1, self._y2))
        right_wall = Line(Point(self._x2, self._y1),Point(self._x2, self._y2))
        top_wall = Line(Point(self._x1, self._y1),Point(self._x2, self._y1))
        bottom_wall = Line(Point(self._x1, self._y2),Point(self._x2, self._y2))

        if self.has_left_wall:
            self._win.draw_line(left_wall, line_color)
        else:
            self._win.draw_line(left_wall, "blue")

        if self.has_right_wall:
            self._win.draw_line(right_wall, line_color)
        else:
            self._win.draw_line(right_wall, "blue")

        if self.has_top_wall:
            self._win.draw_line(top_wall, line_color)
        else:
            self._win.draw_line(top_wall, "blue")

        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall, line_color)
        else:
            self._win.draw_line(bottom_wall, "blue")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        start = Point(
            (self._x1 + self._x2)//2,
            (self._y1 + self._y2)//2
        )
        finish = Point(
            (to_cell._x1 + to_cell._x2)//2,
            (to_cell._y1 + to_cell._y2)//2
        )

        self._win.draw_line(Line(start, finish), color)
