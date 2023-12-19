# create a class Robot
class Robot:
    num_of_robot = 0                 # create a variable that counts the number of robots

    # initialize the data (robot instance) with a name

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))

        Robot.num_of_robot += 1      # current number of robots

    def die(self):
        print("{} is now being destroyed!".format(self.name))

        Robot.num_of_robot -= 1

        if Robot.num_of_robot > 0:
            print("There are still {:d} robots functional.".format(Robot.num_of_robot))

        else:
            print("{} was the last robot here.".format(self.name))

    
    def say_hello(self):
        print("My builders call me {}.".format(self.name))

    @classmethod
    def how_many(n):
        print("Currently, there are {:d} robots here.".format(n.num_of_robot))


print("\nRobots are a great help in serious tasks\n")

print(".................................................................\n")
print(".................................................................\n")


Robotor_1 = Robot('AK-mars')
Robotor_1.say_hello()
Robotor_1.how_many()

print(".................................................................\n")
print(".................................................................\n")

Rabat2k1 = Robot('FR-MJ')
Rabat2k1.say_hello()
Rabat2k1.how_many()

print(".................................................................\n")
print(".................................................................\n")

print("Robots have now finished thir work. We can start desroying them.\n")
Robotor_1.die()
Rabat2k1.die()

print(".................................................................\n")
print(".................................................................\n")

Robot.how_many()