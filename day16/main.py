from prettytable import PrettyTable

table = PrettyTable()

# Use add_column instead of add.column
table.add_column("Pokemon Name", ["Pikachu", "Squirrel", "Charmane"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

# class User:
#     pass
# user_1= User()
# user_1.id = "001"
# user_1.username = "khushi"
# print(user_1.username)
# print(user_1.id)