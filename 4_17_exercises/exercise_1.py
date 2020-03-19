directions = ["N", "E", "S", "W"]


def turn_clockwise(direction):
     current_direction = directions.index(direction)
     return directions[(current_direction + 1) % len(directions)]


def turn_counter_clockwise(direction):
    current_direction = directions.index(direction)
    return directions[(current_direction - 1) % len(directions)]


print(turn_clockwise("E") == "SE")
