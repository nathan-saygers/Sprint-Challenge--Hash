def get_indices_of_item_weights(weights, length, limit):
    # address edge cases (2 or fewer items)
    if length < 2:
        return None

    if length == 2:
        if weights[0] + weights[1] == limit:
            return [1, 0]
    # Declare a weights dict and results tuple
    wd = {}
    result = []
    # loop a range with index and length as upper limit
    for i in range(0, length):
        # save each index as a value, with (limit - num) as key
        wd[limit - weights[i]] = i

    # print('weight dict:', wd)
    # loop over weights arr:
    for num in weights:
        # if a weight in the array == wd[index] these are a pair
        if num in wd.keys():
            # get index of num
            result.append(wd[num])
            # return the index of the weight and the key from wd

    return result


get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)


# [4, 6, 10, 15, 16]
