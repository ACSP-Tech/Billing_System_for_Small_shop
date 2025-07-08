from datetime import datetime

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = quantity * price
        self.date = datetime.now().isoformat()

    def add_to_record(self, record_dict):
        record_dict["name"].append(self.name)
        record_dict["price"].append(self.price)
        record_dict["quantity"].append(self.quantity)
        record_dict["total"].append(self.total)
        record_dict["date"].append(self.date)


