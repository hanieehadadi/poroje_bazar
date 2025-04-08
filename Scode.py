#product list 
products= [{"id": 1, "name": "laptop", "price": 250, "stock": 6},
{"id ": 2, "name": "camera", "price":300, "stock": 28}]


def show_menue():
    print("show all product")

def show_product():
    print("/n product list")
    for product in products:
        print(f"id:{product["id"]}, name:{product["name"]}")