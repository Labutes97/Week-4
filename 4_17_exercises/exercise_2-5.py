day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


# exercise 2
def day_name(day_number):

    # check input
    if day_number < 0 or day_number > 6:
        return None

    return day_names[day_number]


# exercise 3
def day_num(convert_day_name):

    # check input
    if convert_day_name not in day_names:
        return None

    return day_names.index(convert_day_name)


# exercise 4
def day_add(start_day_name, delta):
    start_day_number = day_num(start_day_name)

    if start_day_number is None:
        return None

    end_day = day_name((start_day_number + delta) % 7)
    return end_day


# tests

# exercise 2
print(day_name(0) == "Sunday")
print(day_name(6) == "Saturday")
print(day_name(8) is None)

# exercise 3
print(day_num("Sunday") == 0)
print(day_num("March") is None)

# exercise 2 and 3 combined
print(day_name(day_num("Wednesday")) == "Wednesday")
print(day_num(day_name(2)) == 2)

# exercise 4
day_add("Monday", 4) ==  "Friday"
day_add("Tuesday", 0) == "Tuesday"
day_add("Tuesday", 14) == "Tuesday"
day_add("Sunday", 100) == "Tuesday"

# exercise 5
day_add("Sunday", -1) == "Saturday"
day_add("Sunday", -7) == "Sunday"
day_add("Tuesday", -100) == "Sunday"
