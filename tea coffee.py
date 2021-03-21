class tea_coffee:
    def __init__(self,customer):
        self.customer=customer
    def tea(self):
        dict = {}
        self.ginger=input("how many ginger slices do you want to add?: ")
        self.sugar=input("how many spoons of sugar do you want?: ")
        self.milk=input("do you want milkless tea(y/n)?: ")
        dict.update({self.customer: [self.ginger, self.sugar, self.milk]})
        print(dict)
    def coffee(self):
        dict = {}
        self.cold=input("you want hot(h) or cold(c) coffee?: ")
        self.strength=input("you want mild(m) or stong(s) coffee?: ")
        self.sugar = input("do you want sugar(y/n)?: ")
        dict.update({self.customer: [self.cold, self.strength, self.sugar]})
        print(dict)

print("WELCOME")
c=tea_coffee(input("Enter your name: "))
tc=input("do you want to have tea(t) or coffee(c): ")
if(tc== "t"):
    c.tea()
elif(tc=="c"):
   c.coffee()
else:
    print("Invalid choice!")
input("Are you sure about your choices(y/n)?: ")
print("THANK YOU")