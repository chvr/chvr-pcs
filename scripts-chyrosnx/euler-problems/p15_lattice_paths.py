import os
from enum import Enum
from queue import LifoQueue


__author__ = 'ChyrosNX'


class Path(Enum):
    up = 0
    right = 1
    down = 2
    left = 3


class Intersection:

    def __init__(self, open_paths):
        self._paths = open_paths
        self._closed_paths = []
        self._used_path = None

    def get_all_paths(self):
        return self._paths

    def get_open_paths(self):
        open_paths = []
        for p in self._paths:
            if p not in self._closed_paths:
                open_paths.append(p)

        return open_paths

    def get_used_path(self):
        return self._used_path

    def use_path(self, path):
        if path in self.get_open_paths():
            self._closed_paths.append(path)
            self._used_path = path

    def reset(self):
        self._closed_paths.clear()
        self._used_path = None


class Grid:

    def __init__(self, columns=2, rows=2, allowed_paths=[Path.up, Path.right, Path.down, Path.left], verbose=False):
        self._columns = columns
        self._rows = rows
        self._allowed_paths = allowed_paths
        self._verbose = verbose

        self._pos_x = 0
        self._pos_y = 0
        self._move_history = LifoQueue()
        self._last_move = None

        self._create_grid_matrix()

    def _create_grid_matrix(self):
        self._grid_matrix = []
        for r in range(0, self._rows + 1):
            self._grid_matrix.append([])
            for c in range(0, self._columns + 1):
                open_paths = []
                if Path.up    in self._allowed_paths and r > 0            : open_paths.append(Path.up)
                if Path.right in self._allowed_paths and c < self._columns: open_paths.append(Path.right)
                if Path.down  in self._allowed_paths and r < self._rows   : open_paths.append(Path.down)
                if Path.left  in self._allowed_paths and c > 0            : open_paths.append(Path.left)
                self._grid_matrix[r].append(Intersection(open_paths))

    def get_intersection(self):
        return self._grid_matrix[self._pos_y][self._pos_x]

    def get_open_paths(self):
        return self._grid_matrix[self._pos_y][self._pos_x].get_open_paths()

    def backtrack(self):
        if self._move_history.empty():
            if self._verbose:
                print('! No more paths to backtrack from.')
            return False

        self._last_move = self._move_history.get()
        self.get_intersection().reset()

        if   self._last_move == Path.up   : self._pos_y += 1
        elif self._last_move == Path.right: self._pos_x -= 1
        elif self._last_move == Path.down : self._pos_y -= 1
        elif self._last_move == Path.left : self._pos_x += 1
        else:
            if self._verbose:
                print('! Unable to backtrack anymore.')
            return False

        return True

    def move(self, path=None):
        open_paths = self.get_open_paths()
        if self._last_move is not None and self._last_move in open_paths:
            open_paths.remove(self._last_move)
            self._last_move = None

        if path is None:
            if len(open_paths) > 0:
                path = open_paths[0]
            else:
                if self._verbose:
                    print('! No more open paths to move into.')
                return False
        elif path not in open_paths:
            if self._verbose:
                print('! Unable to move {}.'.format(path.name))
            return False

        self.get_intersection().use_path(path)
        self._move_history.put(path)

        if   path == Path.up   : self._pos_y -= 1
        elif path == Path.right: self._pos_x += 1
        elif path == Path.down : self._pos_y += 1
        elif path == Path.left : self._pos_x -= 1

        return True

    def is_at_start(self):
        return self._pos_x == self._pos_y == 0

    def is_at_end(self):
        return self._pos_y == self._rows and self._pos_x == self._columns

    def _to_string(self):
        COL_WIDTH = 3
        ROW_HEIGHT = 1

        output = ''
        for r in range(0, self._rows + 1):
            for c in range(0, self._columns + 1):
                if self._pos_y == r and self._pos_x == c:
                    area = 'x'
                else:
                    path = self._grid_matrix[r][c].get_used_path()
                    if path == Path.up:
                        area = '^'
                    elif path == Path.right:
                        area = '>'
                    elif path == Path.down:
                        area = 'v'
                    elif path == Path.left:
                        area = '<'
                    else:
                        area = '+'

                if c < self._columns:
                    area += ''.rjust(COL_WIDTH, '-')

                output += area

            if r < self._rows:
                for h in range(0, ROW_HEIGHT):
                    output += os.linesep
                    for c in range(0, self._columns + 1):
                        output += '|'
                        if c < self._columns:
                            output += ''.rjust(COL_WIDTH, ' ')

            if r < self._rows:
                output += os.linesep

        return output

    def __str__(self):
        return self._to_string()

    def __repr__(self):
        return self._to_string()


class Main:

    def __init__(self):
        pass

    def start(self, width, height):
        print('Depending on the given X by X grid, calculating routes may take a while...{}'.format(os.linesep))

        _grid = Grid(width, height, allowed_paths=[Path.right, Path.down])
        routes = 0

        while not (_grid.is_at_start() and len(_grid.get_open_paths()) == 0):
            _grid.move()
            if _grid.is_at_end():
                routes += 1
                print('Route #{}{}{}{}'.format(routes, os.linesep, _grid, os.linesep, os.linesep))

                while not _grid.is_at_start():
                    _grid.backtrack()
                    has_avail_paths = len(_grid.get_intersection().get_all_paths()) > 1 and len(_grid.get_open_paths()) > 0
                    if has_avail_paths:
                        break

        print('There were {} possible routes for {}x{} grid.'.format(routes, width, height))

main = Main()
main.start(5, 5)
