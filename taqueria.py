dict_menu_entrees = {
                     "Baja Taco":        4.25,
                     "Burrito":          7.50,
                     "Bowl":             8.50,
                     "Nachos":           11.00,
                     "Quesadilla":       8.50,
                     "Super Burrito":    8.50,
                     "Super Quesadilla": 9.50,
                     "Taco":             3.00,
                     "Tortilla Salad":   8.00
                     }

total = 0

while True:
    try:
        entree_desired = input("Item: ").lower()
        if not entree_desired.strip():
            raise EOFError

        for entrees in dict_menu_entrees:
            if entrees.lower() == entree_desired:
                total += dict_menu_entrees[entrees] # Adds item's price to client tab
                print(f'Total: ${total:.2f}')

    except EOFError:
        break
