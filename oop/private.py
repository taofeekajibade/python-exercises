class School:
    def __init__(self, name=None, model=None, year=None):
        self.__name = name
        self.__model = model
        self.__year = year

    def say_hi(self):
        if self.__name:
            print(f"Hello, I am {self.__name}")
        else:
            print("Hello, I do not know my own name")
        if self.__model:
            print(f"My model is {self.__model}")
        else:
            print("I am sorry I have no model.")
        if self.__year:
            print(f"I was established in {self.__year}")
        else:
            print("I can not remember my year.")

        def set_name(self, name):
            self.__name = name

        def get_name(self):
            return self.__name

        def set_model(self, model):
           self.__model = model

        def get_model(self):
            return self.__model

        def set_year(self, year):
           self.__year = year

        def get_year(self):
            return self.__year

a = School("Kiddies", "private", 2015)
b = School("Alfalah")
c = School()
c.set_model("new")

print(a.say_hi())
print(b.say_hi())
print(c.say_hi())


