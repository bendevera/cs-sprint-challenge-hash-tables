def intersection(arrays):
    """
    YOUR CODE HERE
    """
    array_count = len(arrays)
    counter = {}
    array_counter = {}

    for array in arrays:
        for i in range(len(array)):
            if array[i] not in array_counter:
                if array[i] in counter:
                    counter[array[i]] += 1
                else:
                    counter[array[i]] = 1
        array_counter = {}
    
    result = [key for (key, value) in counter.items() if value == array_count]
    print(result)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
