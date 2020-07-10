def has_negatives(a):
    """
    YOUR CODE HERE
    """
    counter_parts = {}
    result = []

    for number in a:
        if number < 0:
            counter_part = abs(number)
            if counter_part in counter_parts:
                result.append(counter_part)
        else:
            counter_part = number * -1
            if counter_part in counter_parts:
                result.append(number)
        counter_parts[number] = True

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
