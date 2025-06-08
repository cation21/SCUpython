#Pyramid pattern
def pyramid(n):
    for row in range(1, n + 1):
        # Print spaces
        for space in range(n - row):
            print(" ", end="")
        # Print stars
        for star in range(2 * row - 1):
            print("*", end="")
        print()
