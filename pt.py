from prettytable import PrettyTable

table = PrettyTable()

# Use add_column instead of add.column
table.add_column("Pokemon Name", ["Pikachu", "Squirrel", "Charmane"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
