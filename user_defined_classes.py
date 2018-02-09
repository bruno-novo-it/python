class Worker:
    def __init__(self, name, pay):      # Initial function
        self.name = name
        self.pay = pay
    def firstName(self):                # Split string on blanks and get first
        return self.name.split()[0]
    def lastName(self):                 # Split string on blanks and get last
        return self.name.split()[-1]
    def giveRaise(self, percent):       # Update pay in + x%
        self.pay *= (1.0 + percent)
    def takeRaiseOut(self,percent):     # Update pay in - x%
        self.pay -= (self.pay * percent)

bruno = Worker('Bruno Luis',50000)
nathan = Worker('Nathan Silva', 60000)

print(bruno.firstName())               # Print First Name (Function)

print(bruno.lastName())                # Print Last name (Function)

print(nathan.firstName())

print(nathan.lastName())

nathan.giveRaise(.10)                   # Give 10% Raise

print(nathan.pay)                       # Print updated payment

nathan.takeRaiseOut(.10)                # Take 10% Out

print(nathan.pay)
