class Bag:
    def __init__(self):
        self.items = []
        self.total = f"Total items is {self.items}"

    def add(self, x):
        self.items.append(x)

    def add_item(self, x):
        self.add(x)
        return self.items
        print(self.total)

Akin = Bag()
W = Bag()
print(W.add_item('Agbado'))
print(Akin.add_item("gaari"))

