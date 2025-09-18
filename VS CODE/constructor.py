class example:
    def __init__(self , a= 0, b =0):
        self.a = a
        self.b = b

    def calculateData(self , el):
        self.a = el.a + self.a
        self.b = el.b + self.b
    def displayData(self):
        print("A:", self.a)
        print("B:", self.b)

el = example(5, 10)
e2 = example(15, 20)

e2.calculateData(el)
e2.displayData()