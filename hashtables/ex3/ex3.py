def intersection(arrays):
    # create a frequency dictionary
    frequency_dict = {}
    result = []
    # loop through array
    for arr in arrays:
        # for each array, increment the dictionary entry for the elements
        for char in arr:
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
    # if the frequency in the dictionary is equal to the array's length, append to output array
    items = frequency_dict.items()
    for item in items:
        if item[1] == len(arrays):
            result.append(item[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
