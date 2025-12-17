# OOP Explanation


class Saint:
    # class attributes
    god = "Athena"

    def __init__(self, name, range, constelation):

        # Attributes instances
        self.name = name
        self.range = range
        self.constelation = constelation

    # Methods instances
    def intro(self):
        return f"I am a {self.god} saint. My constelation is {self.constelation}"


# Sub class
class Bronze(Saint):
    father = "Mitsumasa Kido"

    def attack(self):
        return "Hit 100 points"

    def intro(self):
        print(super().intro())  # store it in a value or print i
        return f"My name is Pegasus Seiya. And my father is {self.father}"


# Sub class
class Gold(Saint):

    # Completely override the attack() method
    def attack(self):
        return "Hit 500 points"

    # call the parent intro() and extend the method
    def intro(self):
        print(super().intro())  # store it in a value or print it
        return f"I am {self.name}, The strongest gold saint."


seiya = Bronze("seiya", "bronze", "pegasus")
saga = Gold("saga", "gold", "gemini")
kanon = Gold("kanon", "gold", "gemini")

print(seiya)
# print(saga.intro())
