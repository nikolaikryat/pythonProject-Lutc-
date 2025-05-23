class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)

x = bob.lastName()
y = sue.lastName()
print(x)
print(y)

z = sue.giveRaise(.10)
print(sue.pay)