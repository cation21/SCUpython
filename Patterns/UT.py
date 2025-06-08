#Upper triangle pattern
def LT(n):
    for row in range(1,n+1):
        for col in range(row):
            print("*", end="")
        print()

