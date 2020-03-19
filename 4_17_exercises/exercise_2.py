day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def day_name(day_number):

    # check input
    if day_number < 0 or day_number > 6:
        return None

    return day_names[day_number]


# tests
print(day_name(0) == "Sunday")
print(day_name(6) == "Saturday")
print(day_name(8) is None)
