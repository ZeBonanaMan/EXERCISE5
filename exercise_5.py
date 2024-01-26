def number_set(compare):
    first_number = compare[0]
    last_number = compare[-1]

    if first_number == last_number:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]

print("Given list:", list(numbers_x))
print("result is", number_set(numbers_x))

numbers_y = [75, 65, 35, 75, 30]

print("Given list:", numbers_y)
print("result is", number_set(numbers_y))