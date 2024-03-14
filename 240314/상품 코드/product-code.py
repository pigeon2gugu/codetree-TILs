a, b = tuple(input().split())

class Item :
    def __init__(self, name = "", code = "") :
        self.name = name
        self.code = code


item1 = Item()
item2 = Item()
items = [item1, item2]

item1.name = "codetree"
item1.code = "50"

item2.name = a
item2.code = b

for item in items :
    print(f"product {item.code} is {item.name}")