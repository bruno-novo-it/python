class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name  = last_name
        self.eye_color = eye_color
    
    def show_info(self):
        print("Last Name: {}".format(self.last_name))
        print("Eye Color: {}".format(self.eye_color))

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

billy_cyrus = Parent("Cyrus", "Blue")

print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "Blue", 5)

print(miley_cyrus.number_of_toys)

miley_cyrus.show_info()


