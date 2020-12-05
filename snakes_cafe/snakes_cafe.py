def print_welcome_msg():
    welcome_msg = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************"""
    print(welcome_msg)

def print_cat():
    cat = [
    {
        "name": "Appetizers",
        "items": [
            "Wings",
            "Cookies",
            "Spring Rolls",
        ],
    },
    {
        "name": "Entrees",
        "items": [
            "Salmon",
            "Steak",
            "Meat Tornado",
            "A Literal Garden",
        ],
    },
    {
        "name": "Desserts",
        "items": [
            "Ice Cream",
            "Cake",
            "Pie",
        ],
    },
    {
        "name": "Drinks",
        "items": [
            "Coffee",
            "Tea",
            "Unicorn Tears",
        ],
    },
    ]

    for x in range(len(cat)):
        print(cat[x]["name"])
        print("----------")
        for y in range(len(cat[x]["items"])):
            print(cat[x]["items"][y])
        print("                 ")

    print("***********************************")

if __name__ == "__main__":
    print_welcome_msg()
    print_cat()

    input_msg = """
** What would you like to order? **
***********************************

    """
    print(input_msg)

    user_input =" "
    order_dictionary={}

    while user_input!="quit":
        
        user_input=input(">")
        ItemChecked=user_input.lower()
        if ItemChecked in order_dictionary:
            order_dictionary[ItemChecked]+=1
        else:
            order_dictionary[ItemChecked]=1
        
        if ItemChecked == "quit":
            print("Hope you are enjoyed in our resturant")
        else:
            print(f"*** {order_dictionary[user_input.lower()]}  order of {ItemChecked} have been added to your meal ***")
