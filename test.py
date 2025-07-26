shopping_lt = []

while True:
    item = input(f"\nShopping list: {shopping_lt}\nPress q to exit\nEnter item to add: ")
    if item == 'q':
        break
    shopping_lt.append(item)
print("List insertion mode exited!\n\n")

while True:
    item = input(f"\nShopping list: {shopping_lt}\nPress q to exit\nEnter item to remove: ")
    if item == 'q':
        break
    if len(shopping_lt) == 0:
        print("List is empty\n")
        break
    if item not in shopping_lt:
        print("Item not in the list\n\n")
        continue
    shopping_lt.remove(item)