# create a class Robot
class Robot:
    """ create a class variable that counts the number of robots """
    num_of_robot = 0

    # initialize the data (robot instance) with a name

    def __init__(self, name):
        self.name = name
        print(f"(Initializing {self.name}).")

        Robot.num_of_robot += 1     # current number of robots

    def die(self):
        print(f"{self.name} is now being destroyed!")

        Robot.num_of_robot -= 1

        if Robot.num_of_robot > 0:
            print(f"There are still {Robot.num_of_robot} robots functional.")

        else:
            print(f"{self.name} was the last robot here.")

    
    def say_hello(self):
        print(f"My builders call me {self.name}.")

    @classmethod
    def how_many(n):
        print(f"Currently, there are {n.num_of_robot} robots here.")


print("\nRobots are a great help in serious tasks\n")

print() # print a blank line

Robotor_1 = Robot('AK-mars')
Robotor_1.say_hello()
Robotor_1.how_many()

print() # print a blank line

Rabat2k1 = Robot('FR-MJ')
Rabat2k1.say_hello()
Rabat2k1.how_many()

print() # print a blank line

print("Robots have now finished their work. We can start desroying them.\n")
Robotor_1.die()
Rabat2k1.die()

print() # print a blank line

Robot.how_many()