def has_negatives(a):
    # create frequency dictionary and result array
    freq_dict = {}
    result = []
    # loop over input array
    for num in a:
        # account for zero
        if num == 0:
            continue
        # if the key already exists, add the value of the integer to the existing value
        elif abs(num) in freq_dict:
            freq_dict[abs(num)] = freq_dict[abs(num)] + num
        # save the absolute value of each integer as the key, normal value as value
        else:
            freq_dict[abs(num)] = num
    # use items function on frequency array
    items = freq_dict.items()
    # loop over items array
    for item in items:
        if item[1] == 0:
            # append to result if char[val] is 0
            result.append(item[0])

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
