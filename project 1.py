class product:
    def __init__(self,Id,Name,Category,Quantity,Price):
        self.id= Id
        self.name = Name
        self.category = Category
        self.quantity = Quantity
        self.price = Price

    def basedOnCategory(self, Category):
        data = dict(zip(self.name,self.category))
        have = 0
        for name,cat in data.items():
            if cat.lower() == Category.lower():
                print("product name is:",name)
                have = 1
        if have == 0:
            print("No items found with that category")

    def basedOnQuantity(self,Quantity):
        data = dict(zip(self.name,self.quantity))
        have = 0
        for name,quantity in data.items():
            if quantity == Quantity:
                print("product name is:",name)
                have = 1
        if have == 0:
            print("No items found with that quantity")

Id = []
Name = []
Category = []
Quantity = []
Price = []

print("Welcome to Market")
cart = int(input("How many products want:"))

for i in range(1,cart+1):

    id = int(input(f" product id:"))
    name = input(f" Name of the Product:")
    category = input(f" product category:")
    quantity = int(input(f"product Quantity:"))
    price = int(input(f" product price:"))
    
    Id.append(id)
    Name.append(name)
    Category.append(category)
    Quantity.append(quantity)
    Price.append(price)

p1 = product(Id,Name,Category,Quantity,Price)
mark=0
while mark==0:
    print("Enter 1.Category \n2.Quantity")
    choice = int(input("Enter choice:"))
    if choice == 1:
        details = input("Enter Category:")
        p1.basedOnCategory(details)
    else:
        details = int(input("Enter Quantity:"))
        p1.basedOnQuantity(details)
    cointune=int(input("enter the choice to cointinu 1,exit 2"))
    if cointune==1:
        pass
    elif cointune==2:
        mark=1
    else:
        print("entet the valide choice to enter")