class simple:
    def __init__(self):
        self.name = "Salman"
        self._age = 50
        self.__balance = 987654321
s = simple()
print(s.name)
print(s._age)
print(s._simple__balance)