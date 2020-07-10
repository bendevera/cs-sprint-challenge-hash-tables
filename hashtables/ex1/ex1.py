def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    matches = {}

    for i in range(len(weights)):
        match = limit - weights[i]
        if match in matches:
            if matches[match] > i:
                return (matches[match], i)
            else:
                return (i, matches[match])
        else:
            matches[weights[i]] = i
    
    return None
