#inventory management system

class product:
    def __init__(self,pid,name,price,stock):
        self.pid=pid
        self.name=name
        self.price=price
        self.stock=stock

class order:
    def __init__(self,oid,product,qty):
        self.oid=oid
        self.product=product
        self.qty=qty
        self.status="PLACED"

class inventory:
    def __init__(self):
        self.products = {}
        self.orders = {}
    
    def add_product(self,product):
        self.products[product.pid]=product
    
    def place_order(self,oid,pid,qty):
        if pid not in self.products:
            print("product not found")
            return
        product=self.products[pid]
        if product.stock < qty:
            print ("out of stock")
            return
        product.stock-=qty
        new_order=order(oid,product,qty)
        self.orders[oid]=new_order
        print ("order placed successfully")

    def cancel_order(self,oid):
        if oid not in self.orders:
            print("order not found")
            return
        
        order=self.orders[oid]
        order.status="CANCELLED"
        order.product.stock+=order.qty
        print("order cancelled")
    

inv = inventory()
while True:
    print("1. add product")
    print("2. place order")
    print("3. cancel order")
    print("4. exit")

  
    choice = int(input("enter your choice: "))
    if choice == 1:
        pid=int(input("enter the product id: "))
        name=input("enter name of the product: ")
        price=int(input("enter price of the product: "))
        stock=int(input("enter stock: "))
        p=product(pid,name,price,stock)
        inv.add_product(p)
        print("product added sucessfully")

    if choice == 2:
        oid=int(input("enter order id: "))
        pid=int(input("enter the product id: "))
        qty=int(input("enter qyantity of the product: "))
        
        inv.place_order(oid,pid,qty)
        print("order placed successfully")

    if choice == 3:
        oid=int(input("enter order id: "))
        inv.cancel_order(oid)
        print("order cancelled successfully")

    if choice == 4:
        print("exitting system...")
        break
    else:
        print("invalid choice")
