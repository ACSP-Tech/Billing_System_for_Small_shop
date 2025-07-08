
def check_filepath():
    import os
    from models import Product
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    try:
        import json
        billing_objects = {
            "name" : [],
            "price" : [],
            "quantity" : [],
            "total" : [],
            "date" : []
        }
        file_path1 = os.path.join(BASE_DIR, "billing_record.json")
        if not os.path.exists(file_path1):
            with open(file_path1, "x") as file:
                json.dump(billing_objects, file)
        else:
            print("json file called billing_record already exits")
            print()
    except Exception as e:
        print(f"Error with the code: {e}")
    

    
def menu():
    print(".............................................................")
    print()
    print("...     Welcome to ACSP Billing System for Small Shop  ......")
    print("...    Enter a valid interger from the menu options below....")
    num = 1
    menulist = ["Add product to cart", "View cart and total",  "Apply discount if total", "Save bill to file", "View previous transactions", "exit"]
    for menu in menulist:
        print()
        print(f"{num}. {menu}")
        num += 1
    while True:
        try:
            options = int(input("Enter:  \n"))
            if options > 6:
                print("Kindly choose from the option above")
                print()
                continue
            elif options < 1:
                print("Kindly choose from the option above")
                print()
                continue
            else:
                break
        except:
            print("Please Enter a valid Integer")
            print()
            continue
    return options      


class Cart:
    def add_option(self):
        import json
        import os
        from models import Product
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, "billing_record.json")
        with open(file_path, "r") as file:
            old_json = json.load(file)
        while True:
            try:
                name = input("Enter your product name info: \n").strip().lower()
                price = float(input(f"Enter the price of product {name}: \n"))
                quantity = int(input(f"Enter a whole number for quantity: \n"))
            except Exception as e:
                print(f"Error with the code: {e}")
                continue  
            #create an billing object
            billing_objects = Product(name, price, quantity)
            #add billing to the object 
            billing_objects.add_to_record(old_json)
            with open(file_path, "w") as file:
                json.dump(old_json, file)
                print(f"{name} sucessully added to cart!")
                break


    def view_option(self):
        import json
        import os
        from models import Product
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, "billing_record.json")
        with open(file_path, "r") as file:
            old_json = json.load(file)
        import pandas as pd
        view = pd.DataFrame(old_json)
        grand_total = view['total'].sum()
        print(f"the grand_total for cart is {grand_total}")
        return print(view)

    def save_to_file(self):
        while True:
            try:
                import json
                import os
                from models import Product
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(BASE_DIR, "billing_record.json")
                #read cart
                with open(file_path, "r") as file:
                    old_json = json.load(file)
                file_path1 = os.path.join(BASE_DIR, "saved_record.json")
                #save cart to file
                with open(file_path1, "w") as file:
                            json.dump(old_json, file)
                import pandas as pd
                view = pd.DataFrame(old_json)
                grand_total = view['total'].sum()
                print(f"your cart bill has been succesfully saved as saved_record.json and your cart cleared!!! \n{view} \nthe grand total is {grand_total}")
                #read previous transaction
                file_path2 = os.path.join(BASE_DIR, "previous_record.json")
                with open(file_path2, "r") as file:
                    previous_json = json.load(file)
                print("previous record read")
                #append current transaction to previous transaction
                num_billings = len(previous_json["name"])
                for i in range(num_billings):
                    try:
                        name = previous_json["name"][i]
                        price = previous_json["price"][i]
                        quantity = previous_json["quantity"][i]
                        total = previous_json["total"][i]
                        date = previous_json["date"][i]
                        billing_objects = Product(name, price, quantity)
                        #add billing to the object 
                        billing_objects.add_to_record(old_json)
                    except Exception as e:
                        print(f"Error at index {i}: {e}")
                        continue    
                with open(file_path2, "w") as file:
                            json.dump(old_json, file)
                print("previous transaction written successfully")
                #clear cart
                billing_objects = {
                        "name" : [],
                        "price" : [],
                        "quantity" : [],
                        "total" : [],
                        "date" : []
                    }
                with open(file_path, "w") as file:
                    json.dump(billing_objects, file)
                    break
                    print("cart cleared!!!")
            except:
                print("Check and remove all saved_record.json from your directory to be able to download your record")
                continue 


    def apply_discount(self):
        import json
        import os
        from models import Product
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(BASE_DIR, "billing_record.json")
        with open(file_path, "r") as file:
            old_json = json.load(file)
        for i in  old_json['total']:
            index = old_json['total'].index(i)
            total = old_json['total'][index]
            if total > 10000:
                discount = i * 0.1
                old_json['total'][index] -= discount
            else:
                continue
        with open(file_path, "w") as file:
            json.dump(old_json, file)
        print(f"discount sucessully added to cart! \n view cart below")
        import pandas as pd
        view = pd.DataFrame(old_json)
        print()
        return print(view)
            
                
    def load_previous_trans(self):
        import json
        import os
        from models import Product
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        file_path =  os.path.join(BASE_DIR, "previous_record.json")
        with open(file_path, "r") as file:
            old_json = json.load(file)
        import pandas as pd
        view = pd.DataFrame(old_json)
        grand_total = view['total'].sum()
        print(f"All your previous transaction are below \nthe grand_total for all cart previous transaction is {grand_total}")
        return print(view)