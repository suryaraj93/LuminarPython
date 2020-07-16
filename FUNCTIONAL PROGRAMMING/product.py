class product:
    def __init__(self,id,name,category,price):
        self.id=id
        self.name=name
        self.category=category
        self.price=price


    def __str__(self):
        return self.name

lst=[]
ob=lst.append(product(100,"id","shoe",2000))
ob=lst.append(product(101,"log","key",200))
ob=lst.append(product(102,"iphone","phone",50000))
for item in lst:
    print(item)

price=list(filter(lambda product:product.price>500,lst))
for value in price:
    print(value)