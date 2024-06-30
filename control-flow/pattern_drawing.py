pattern_size = int(input("Enter the size of the pattern: "))
row = 0
while row < pattern_size:
    column = 0
    for column in range(1, pattern_size +1):
        print("*", end="")
    print()
    row+=1
