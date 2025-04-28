class Customer:
    def __init__(self, id: int, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email
        self.id = id
        self.motorcycles = []

    def buy_bike(self, motorcycle):
        self.motorcycles.append(motorcycle)
        print("Motorcycle purchased")


class DealershipCustomer:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer: object):
        self.customers[customer.id] = customer
        print(f"Customer {customer.name} was added")
    
    def get_customer_info(self, customer_id: int):
        if customer_id in self.customers.keys():
            for k, v in self.customers.items():
                if k == customer_id:
                    print(f"Customer information: Name: {v.name} Age: {v.age} Email: {v.email}")
                    return None
                print("Not found")
        else:
            print("Invalid ID")
