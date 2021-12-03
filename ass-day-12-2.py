class Boat:
    _x = 0
    _y = 0
    _waypoint_x = 0
    _waypoint_y = 0

    _direction_idx = 0
    _directions = ['N', 'E', 'S', 'W']

    def __init__(self, position, waypoint, direction):
        self._x, self._y = position
        self._waypoint_x, self._waypoint_y = waypoint
        self._direction_idx = self._directions.index(direction)

    def get_position(self):
        return self._x, self._y

    def get_waypoint(self):
        return self._waypoint_x, self._waypoint_y

    def get_manhattan_distance(self):
        return abs(self._x) + abs(self._y)

    def get_direction(self):
        return self._directions[self._direction_idx]

    def move_north(self, units):
        self._waypoint_y -= units

    def move_south(self, units):
        self._waypoint_y += units

    def move_west(self, units):
        self._waypoint_x -= units

    def move_east(self, units):
        self._waypoint_x += units

    def move(self, direction, units):
        if direction == 'N':
            self.move_north(units)
        elif direction == 'E':
            self.move_east(units)
        elif direction == 'S':
            self.move_south(units)
        elif direction == 'W':
            self.move_west(units)
        elif direction == 'F':
            self._x += units * self._waypoint_x
            self._y += units * self._waypoint_y

    def rotate(self, direction, degrees):
        degrees = degrees * -1 if direction == 'L' else degrees
        rotation = int((degrees / 90) % 4)

        # Shorter, but more inefficient than writing every single case 1,2,3
        for i in range (1, rotation+1):
            old_x = self._waypoint_x
            old_y = self._waypoint_y
            self._waypoint_x = -1 * old_y
            self._waypoint_y = old_x

# Read input
f = open("ass-day-12-input.txt", "r")
instructions = f.read().split("\n")

boat = Boat((0,0),(10, -1), 'E')

for instruction in instructions:
    command = instruction[:1]
    value = int(instruction[1:])

    if command in  ('R', 'L'):
        boat.rotate(command, value)
    elif command in ('N', 'E', 'S', 'W', 'F'):
        boat.move(command, value)
    else:
        print(f"Unknown command {command}{value}")

print (f"Finished. Boat position={boat.get_position()}. Manhattan distance={boat.get_manhattan_distance()}")




