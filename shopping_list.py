shopping_list = {}

number_of_items = int(input("How many items do you want to add to your shopping list? "))

for i in range(number_of_items):
    item_name = input(f"\nEnter the name of the item #{i + 1}: ")
    quantity = input(f"Enter quantity for {item_name}: ")
    shopping_list[item_name] = quantity

    print("\nYour Shopping List: ")
    for item, quantity in shopping_list.items():
        print(f"{item}: {quantity}")
