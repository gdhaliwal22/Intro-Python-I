# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array.
# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3


def centered_average(arr):
    # I woud set the array and sort it
    arr.sort()
    # then remove the smallest and large
    arr.pop()
    arr.pop(0)
    # Return the divided by the length of the reminaing elements
    return sum(arr) // len(arr)


centered_average([1, 2, 3, 4, 100])
centered_average([1, 1, 5, 5, 10, 8, 7])
centered_average([-10, -4, -2, -4, -2, 0])


# def centered_average(arr):
#     # remove min and max
#     arr.remove(min(arr))
#     arr.remove(max(arr))
#     # Return the sum divided by the length of the remaining elements
#     return sum(arr) // len(arr)
