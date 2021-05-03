menu_dic = {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
    'Entrees': 0,
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A Literal Garden': 0,
    'Desserts': 0,
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0,
    'Drinks': 0,
    'Coffee': 0,
    'Tea': 0,
    'Unicorn Tears': 0
}


def welcomeMessage():
    print("""
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """)


def menu():
    food = """
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    ***********************************
    ** What would you like to order? **
    ***********************************
    """
    print(food)


def notFound(type):
    print(f"""
    ** {type} is not in the menu **
    ***********************************
    ** What would you like to order? **
    ***********************************
    """)


def summary():
    for x in menu_dic:
        if menu_dic[x] > 0:
            print(f"{menu_dic[x]} order of {x} have been added to your meal")
    exit()


def gitOrder():
    user_input = ""
    menu()
    while user_input != "quit":
        user_input = input('>')
        if user_input != "quit":

            if user_input in menu_dic:
                menu_dic[user_input] += 1
                print(
                    f"** {menu_dic[user_input]} order of {user_input} have been added to your meal **")
            else:
                notFound(user_input)
        else:
            summary()




welcomeMessage()
gitOrder()
