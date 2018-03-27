def tree(height):
    """
    Given an arbitrary height, return a Christmas tree pattern
    """
    # validate input
    try:
        height = int(height)
    except:
        raise ValueError("Input is not an integer.")

    # check if we can even draw a tree
    if height <= 0:
        raise ValueError("Input must be positive, and bigger than 0.")

    pattern=''
    for current_height in xrange(height):
        pattern+= " " * (height - current_height - 1)
        pattern+= "*" * (current_height*2 + 1) + "\n"

    return pattern


if __name__ == "__main__":
    user_input = input("Input a height, positive integers only: ")
    print(tree(user_input))