print("Welcome to place the rabbit")
field = [["🍀","🍀","🍀"],["🍀","🍀","🍀"],["🍀","🍀","🍀"]]
print(f"{field[0]}\n{field[1]}\n{field[2]}")

print("Where the rabbit should go? 🐇")

row = int(input("Please choose a row: "))
col = int(input("Please choose a column: "))

field[row-1][col-1] = "🐇"
print(f"{field[0]}\n{field[1]}\n{field[2]}")