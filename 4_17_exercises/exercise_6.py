special_months = ["February"]
short_months = ["April", "June", "September", "November"]
long_months = ["January", "March", "May", "July", "August", "October", "December"]

special_length = 28
short_length = 30
long_length = 31


def days_in_month(month):
    if month in special_months:
        return special_length
    elif month in short_months:
        return short_length
    elif month in long_months:
        return long_length
    else:
        return None


# tests
print(days_in_month("February") == 28)
print(days_in_month("December") == 31)