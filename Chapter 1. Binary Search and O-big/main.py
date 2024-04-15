numbers = [i for i in range(128)]


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (high + low) // 2  # Finding mid
        guess = list[mid]  # Trying to find the necessary item

        if guess == item:  # If guess == item => win
            return mid
        elif guess > item:  # If guess > item, it means that we can start to search again, but the guess is the floor,
            high = mid - 1  # so new high is mid - 1
        elif guess < item:  # If guess < item, then low = mid + 1
            low = mid + 1

    return None  # If there is no needed number, then it means that low is increasing until it reaches high and vice
#  if 128 is the high limit, item = 129, then low is 0, then 64, 96 etc., and reaches 128 => then there is no item


print(binary_search(numbers, 77))  # -> 77
