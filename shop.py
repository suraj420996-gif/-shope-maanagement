#menu list 
menu={
    "pizza":50,
    "pasta":40,
    "burger":60,
    "coffee":30
    }
print("welcome to my shope")
print("pizza:Rs50\npasta:Rs40\nburger:Rs60\ncoffee:Rs30") # in ths line we can inject a template
total_order=0
item_1=input("enter the name of item you want to order :")
if item_1 in menu: # check user input items is avaiable or not in menu
    total_order+=menu[item_1]
    print(f"your order item {item_1} has been added")
else:
    print(f"orderd items {item_1} is not avaiable yet")
another_order= input("do you want to another items ? (Yes/No) ")
if another_order=="Yes":
    item_2= input("enter the second items = ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"items{item_2} is added ")
    else:
        print(f"order items{item_2} is not avaiable ")
print(f"total amount of item is {total_order}")
