def x(height):
    """
    Given an arbitrary height, return an X pattern composed of starts. Height must be odd, and >= 3
    """

    # validate input
    try:
        height = int(height)
    except:
        raise ValueError("Input is not an integer.")

    # Check if odd and larger or equal 3
    if height <= 2 or height%2 == 0:
        raise ValueError("Invalid is invalid. Height must be >= 3 and odd")


    pattern=''
    for i in xrange(height):
        line = [" "] * height
        line[i] = "*"
        line[height - 1 - i] = "*"
        pattern += "".join(line) + "\n"

    return pattern

if __name__ == "__main__":
    user_input = input("Input a height, positive, odd integers only: ")
    print(x(user_input))