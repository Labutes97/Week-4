# exercise 7 and 8
def to_secs(hours, minutes, seconds):
    total_seconds = int(hours * 3600)
    total_seconds += int(minutes * 60)
    total_seconds += int(seconds)
    return total_seconds


# exercise 9_1
def hours_in(seconds):
    return seconds // 3600


# tests

# exercise 7
print(to_secs(2, 30, 10) == 9010)
print(to_secs(2, 0, 0) == 7200)
print(to_secs(0, 2, 0) == 120)
print(to_secs(0, 0, 42) == 42)
print(to_secs(0, -10, 10) == -590)

# exercise 8
print(to_secs(2.5, 0, 10.71) == 9010)
print(to_secs(2.433,0,0) == 8758)

# exercise 9
print(hours_in(9010) == 2)
