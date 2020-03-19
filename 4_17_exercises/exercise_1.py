directions = ["N", "E", "S", "W"]


def turn_clockwise(direction):
    if direction not in directions:
        return None

    current_direction = directions.index(direction)
    return directions[(current_direction + 1) % len(directions)]


def turn_counter_clockwise(direction):
    if direction not in directions:
        return None

    current_direction = directions.index(direction)
    return directions[(current_direction - 1) % len(directions)]


# tests
print(turn_clockwise("E") == "S")
print(turn_clockwise("R") is None)
