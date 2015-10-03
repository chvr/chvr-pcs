import time
import os
from enum import Enum
from queue import Queue


__author__ = 'ChyrosNX'


class Direction(Enum):
    up = 0
    rt = 1
    dn = 2
    lt = 3


class Branch:

    def __init__(self, branch_id=0, start_pos_x=0, start_pos_y=0, directions=None, parent_id=None):
        self._id = branch_id
        self._start_pos_x = start_pos_x
        self._start_pos_y = start_pos_y
        self._directions = directions or []
        self._parent_id = parent_id
        self._destination = False

    def add(self, direction):
        self._directions.append(direction)

    def get_id(self):
        return self._id

    def get_start_pos_x(self):
        return self._start_pos_x

    def get_start_pos_y(self):
        return self._start_pos_y

    def get_directions(self):
        return self._directions

    def get_parent_id(self):
        return self._parent_id

    def is_destination(self):
        return self._destination

    def set_destination(self, value):
        self._destination = value

    def __str__(self):
        self._to_string()

    def __repr__(self):
        self._to_string()

    def _to_string(self):
        return self._directions


class Routes:

    def __init__(self):
        self._next_branch_id = 0
        self._branches = {}

    def create(self, start_pos_x=0, start_pos_y=0, directions=None, parent_id=None):
        last_branch_id = self._next_branch_id
        self._next_branch_id += 1

        self._branches[last_branch_id] = Branch(branch_id=last_branch_id, start_pos_x=start_pos_x, start_pos_y=start_pos_y, directions=directions, parent_id=parent_id)
        return last_branch_id

    def move(self, branch_id, direction):
        self._branches[branch_id].add(direction)

    def get_branch(self, branch_id):
        if branch_id not in self._branches:
            return None

        return self._branches[branch_id]

    def get_routes(self):
        routes = []
        for key in self._branches.keys():
            branch = self._branches[key]
            if branch.is_destination():
                routes.append(branch)

        return routes

    def get_destination(self, branch_id):
        directions = []

        while True:
            branch = self.get_branch(branch_id)

            for direction in reversed(branch.get_directions()):
                if   direction == Direction.up: directions.append('^')
                elif direction == Direction.dn: directions.append('v')
                elif direction == Direction.lt: directions.append('<')
                elif direction == Direction.rt: directions.append('>')

            if branch.get_parent_id() is None:
                break

            branch_id = branch.get_parent_id()

        return reversed(directions)


class Grid:

    def __init__(self, rows=2, columns=2, exclude_directions=None):
        self._rows = rows
        self._columns = columns
        self._pos_x = 0
        self._pos_y = 0
        self._exclude_directions = exclude_directions or []

    def move(self, direction):
        if direction == Direction.up: self._pos_y -= 1
        if direction == Direction.dn: self._pos_y += 1
        if direction == Direction.lt: self._pos_x -= 1
        if direction == Direction.rt: self._pos_x += 1

    def get_open_paths(self):
        open_paths = []
        if Direction.up not in self._exclude_directions and self._pos_y > 0            : open_paths.append(Direction.up)
        if Direction.dn not in self._exclude_directions and self._pos_y < self._rows   : open_paths.append(Direction.dn)
        if Direction.lt not in self._exclude_directions and self._pos_x > 0            : open_paths.append(Direction.lt)
        if Direction.rt not in self._exclude_directions and self._pos_x < self._columns: open_paths.append(Direction.rt)

        return open_paths

    def get_pos_x(self):
        return self._pos_x

    def get_pos_y(self):
        return self._pos_y

    def set_pos(self, x, y):
        self._pos_x = x
        self._pos_y = y

    def is_destination_reached(self):
        return self._pos_x == self._rows and self._pos_y == self._columns


class Main:

    def __init__(self):
        pass

    def start(self, row, columns, verbose=False):
        start_timestamp = self.get_current_ms()

        routes = Routes()
        branch_id_queue = Queue()

        current_branch_id = routes.create()
        grid = Grid(row, columns, exclude_directions=[Direction.up, Direction.lt])

        while True:
            start_pos_x = grid.get_pos_x()
            start_pos_y = grid.get_pos_y()

            open_paths = grid.get_open_paths()
            if len(open_paths) > 1:
                current_parent_id = current_branch_id
                for i in range(0, len(open_paths)):
                    new_branch_id = routes.create(start_pos_x, start_pos_y, [open_paths[i]], current_parent_id)
                    if i == 0:
                        current_branch_id = new_branch_id
                        grid.move(open_paths[i])
                    else:
                        branch_id_queue.put(new_branch_id)
            elif len(open_paths) == 1:
                routes.move(current_branch_id, open_paths[0])
                grid.move(open_paths[0])

            if grid.is_destination_reached():
                routes.get_branch(current_branch_id).set_destination(True)
                if verbose:
                    print('Route ID #{} completed - {}'.format(current_branch_id, ''.join(routes.get_destination(current_branch_id))))

                if branch_id_queue.empty():
                    break

                current_branch_id = branch_id_queue.get()
                route = routes.get_branch(current_branch_id)
                grid.set_pos(route.get_start_pos_x(), route.get_start_pos_y())
                grid.move(route.get_directions()[0])

        elapsed_time = self.get_current_ms() - start_timestamp
        print()
        print('There were {} possible routes for {}x{} grid. - (Elapsed time: {} ms))'.format(len(routes.get_routes()), row, columns, elapsed_time))
        print()

    def get_current_ms(self):
        return int(round(time.time() * 1000))


print('Depending on the given X by X grid, calculating routes may take a while...')
print()

main = Main()
main.start(2, 2, True)
main.start(5, 5, True)
main.start(7, 7, True)
main.start(10, 10, False)
main.start(20, 20, False)
