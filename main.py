#objective:Manage a collection of books that users can borrow and return.
from billing import check_filepath

check_filepath()



def billing_system():
    from billing import menu
    while True:
        option = menu()
        if option == 1:
            from billing import Cart
            my_cart = Cart()
            my_cart.add_option()
            print()
        elif option == 2:
            from billing import Cart
            my_cart = Cart()
            my_cart.view_option()
            print()
        elif option == 3:
            from billing import Cart
            my_cart = Cart()
            my_cart.apply_discount()
            print()
        #saving to Cart clear cart!!! you can view cart previous transaction cart 
        elif option == 4:
            from billing import Cart
            my_cart = Cart()
            my_cart.save_to_file()
        elif option == 5:
            from billing import Cart
            my_cart = Cart()
            my_cart.load_previous_trans()
        else:
            print("bye")
            break

billing_system()

