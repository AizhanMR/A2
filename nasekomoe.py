import hw4

class Nasekomoe(hw4.Tarakany, hw4.Mnogonojka, hw4.Pauk, hw4.Cherv):
    @property
    def __age(self):
        self.__age = self.age

data = Nasekomoe('Akylai', 22)
print(data.name)
print(data.age)

