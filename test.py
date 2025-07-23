shopping_lt = []
while True:
    item = input(f"Shopping list: {shopping_lt}\n(press q to exit)\nEnter item: ")
    if item == 'q':
        break
    shopping_lt.append(item)

while True:
    item = input(f"Shopping list: {shopping_lt}\n(press q to exit)\nEnter the item to remove: ")
    if item == 'q':
        break
    shopping_lt.remove(item)
print(shopping_lt)
    