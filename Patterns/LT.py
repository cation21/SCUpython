#Lower Triangle pattern
def LT(n):
    for row in range(1,n+1):
        for col in range(n-row+1):
            print("*", end="")
        print()
LT(5)