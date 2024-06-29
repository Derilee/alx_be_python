number = int(input("Enter a number to see its multiplication table: "))
for row in range(1, 11):
    result = number * row
    print(f"{number} * {row} = {result}")
