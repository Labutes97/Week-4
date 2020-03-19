day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


# exercise 2
def day_name(day_number):

    # check input
    if day_number < 0 or day_number > 6:
        return None

    return day_names[day_number]


# exercise 3
def day_num(day_name):

    # check input
    if day_name not in day_names:
        return None

    return day_names.index(day_name)


# tests
print(day_name(0) == "Sunday")
print(day_name(6) == "Saturday")
print(day_name(8) is None)

print(day_num("Sunday") == 0)
print(day_num("March") is None)

print(day_name(day_num("Wednesday")) == "Wednesday")
print(day_num(day_name(2)) == 2)
