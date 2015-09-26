import os
from enum import Enum


__author__ = 'ChyrosNX'


class Direction(Enum):
    up = 0
    right = 1
    down = 2
    left = 3


class Grid:

    def __init__(self, columns=2, rows=2, verbose=False):
        self._columns = columns
        self._rows = rows
        self._verbose = verbose
        self._pos_x = 0
        self._pos_y = 0
        self._matrix = []
        self._create()

    def _create(self):
        for r in range(0, self._rows + 1):
            self._matrix.append([])
            for c in range(0, self._columns + 1):
                self._matrix[r].append([0])

    def clone(self):
        _grid = Grid(self._columns, self._rows, self._verbose)
        _grid._pos_x = self._pos_x
        _grid._pos_y = self._pos_y
        _grid._matrix = []
        for r in range(0, self._rows + 1):
            _grid._matrix.append(list(self._matrix[r]))

        return _grid

    def get_directions(self, allowed_directions=[Direction.up, Direction.right, Direction.down, Direction.left]):
        directions = []
        if Direction.up in allowed_directions and self._pos_y > 0:
            directions.append(Direction.up)
        if Direction.right in allowed_directions and self._pos_x < self._columns:
            directions.append(Direction.right)
        if Direction.down in allowed_directions and self._pos_y < self._rows:
            directions.append(Direction.down)
        if Direction.left in allowed_directions and self._pos_x > 0:
            directions.append(Direction.left)

        return directions

    def move(self, direction):
        if direction not in self.get_directions():
            if self._verbose:
                print('! Can\'t move {}.'.format(direction.name))
            return False

        if direction == Direction.up:
            self._matrix[self._pos_y][self._pos_x] = direction
            self._pos_y -= 1
            if self._verbose:
                print(': Move ^ (up)')
        elif direction == Direction.right:
            self._matrix[self._pos_y][self._pos_x] = direction
            self._pos_x += 1
            if self._verbose:
                print(': Move > (rt)')
        elif direction == Direction.down:
            self._matrix[self._pos_y][self._pos_x] = direction
            self._pos_y += 1
            if self._verbose:
                print(': Move v (dn)')
        elif direction == Direction.left:
            self._matrix[self._pos_y][self._pos_x] = direction
            self._pos_x -= 1
            if self._verbose:
                print(': Move < (lt)')
        else:
            print('! Can\'t move - Invalid direction: {}.'.format(direction))
            return False

        return True

    def is_route_completed(self):
        if self._pos_y == self._rows and self._pos_x == self._columns:
            return True

        return False

    def _to_string(self):
        COL_WIDTH = 3
        ROW_HEIGHT = 1

        output = ''
        for r in range(0, self._rows + 1):
            for c in range(0, self._columns + 1):
                if self._pos_y == r and self._pos_x == c:
                    area = 'x'
                else:
                    direction = self._matrix[r][c]
                    if direction == Direction.up:
                        area = '^'
                    elif direction == Direction.right:
                        area = '>'
                    elif direction == Direction.down:
                        area = 'v'
                    elif direction == Direction.left:
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

        allowed_directions = [Direction.right, Direction.down]
        completed_routes = []
        incomplete_routes = []

        _grid = Grid(width, height)
        incomplete_routes.append(_grid)

        while len(incomplete_routes) > 0:
            for grid in incomplete_routes:
                directions = grid.get_directions(allowed_directions=allowed_directions)
                for i in range(0, len(directions)):
                    if i == 0:
                        grid_copy = grid.clone()

                    if i > 0:
                        new_grid = grid_copy.clone()
                        new_grid.move(directions[i])
                        incomplete_routes.append(new_grid)
                    else:
                        grid.move(directions[i])

            for route in incomplete_routes:
                if route.is_route_completed():
                    completed_routes.append(route)
                    incomplete_routes.remove(route)

        counter = 0
        for route in completed_routes:
            counter += 1
            print('Route #{}{}{}{}'.format(counter, os.linesep, route, os.linesep, os.linesep))

        print('There were {} possible routes for {}x{} grid.'.format(len(completed_routes), width, height))

main = Main()
main.start(5, 5)

