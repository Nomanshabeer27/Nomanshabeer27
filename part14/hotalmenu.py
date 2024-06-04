# define the menu of resturant
menu = {
    'Pizza': 400,
    'Pasta': 300,
    'Coffee': 200,
    'Salad': 100,
    'Burgar': 150,
}
print("welcome the python resturant")
print("Pizza: Rs400\nPasta: Rs300\nCoffee: Rs200\nSalad: Rs100\nburgar: Rs150 ")


total_order = 0
item_1 = input("Emter the name of item you want to order = ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Enter the{item_1}has been added the order")

else:
    print(f"Order item{item_1}is not avaliable yet")

another_order = input("do you want to add another item? {yes/no}")
if another_order == "yes":
    item_2 = input("Enter the name of second order item = ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"item {item_2} has been added to second order")
    else:
        print("Order item {item_2} is not avaliable yet")
print(f"The total amount of items to pay is {total_order}")
