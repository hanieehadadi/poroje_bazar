#product list 
products= [{"id": 1, "name": "laptop", "price": 250, "stock": 6},
{"id":4, "name": "Swatch", "price": 26, "stock":28}
,{"id ": 2, "name": "camera", "price":300, "stock": 28},
{"id": 78, "name": "headphone", "price": 6700, "stock": 25}]


def show_menue():
    print("show all product")

def show_product():
    print("/n product list")
    for product in products:
        print(f"id:{product["id"]}, name:{product["name"]}")

import pandas as pd
def show_product_tabel():
    df= pd.Dataframe(products)
    df['stockPrice']= df['cost']* ['stock']
    print("\n-- show tabel ---")
    print(df)
