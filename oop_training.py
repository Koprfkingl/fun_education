# purpose of this file is to demonstrate to myself my OOP abilities
# based on https://www.geeksforgeeks.org/python-oops-concepts/

# create class
class Car:
    # define attributes
    dimensions = 0
    manufacturer = ''
    model = ''

    # now define class function that will create a class instance
    def __init__(self, name):
        print('Initializing new instance of Car class')
        self.name = name

    # define action available to all class instances
    def honk(self):
        print(f'honk:{self.name}')

    def display(self):
        print(f'''Display attributes:
        dimensions: {self.dimensions}
        manufacturer {self.manufacturer}
        model {self.model}''')

# runtime


# create class instances
golf = Car('golf')
focus = Car('focus')
octavia = Car('octavia')

# instance attributes
golf.dimensions = '3532x1754x1512'
golf.manufacturer = 'volkswagen'
golf.model = 'golf'

focus.dimensions = '4469x1896x1455'
focus.manufacturer = 'ford'
focus.model = 'focus'

octavia.dimensions = '4475x1900x1449'
octavia.manufacturer = 'skoda'
octavia.model = 'octavia'

# perform action with class instance
golf.honk()
golf.display()
print('')
focus.honk()
focus.display()
print('')
octavia.honk()
octavia.display()
print('')

# now use attribute in print
print(f'Manufacturer of {golf.model} is {golf.manufacturer}')
print(f'Manufacturer of {focus.model} is {focus.manufacturer}')
print(f'Manufacturer of {octavia.model} is {octavia.manufacturer}')

# access identity of instance
print(f'Name of my first car is {golf.name}')
print(f'Name of my second car {focus.name}')
print(f'Name of my third car {octavia.name}')

# INHERITANCE

class SpecificCar(Car):
    # class attributes
    color = ''
    year = ''
    engine = ''
    fuel = ''
    performance = ''

# class constructor
    def __init__(self, VIN, name):
        self.VIN = VIN

        # invoke parent __init__
        Car.__init__(self, name)

    def break_down(self):
        print(f'{self.name}:Oh no, I am broken, again!')

    def steal(self):
        print(f'{self.name}: Oh no, I have been stolen, again!')

    def ride(self):
        print(f'{self.name}: Oh yeah, I ride like a king, again!')


# create instance
muj_golf = SpecificCar('VK23KB432B21BN2B3','MujGolf')
muj_focus = SpecificCar('NLKGS432NLKNLK33', 'MujFocus')
moje_octavia = SpecificCar('FJDLSK324N32NLN32','MojeOctavia')

muj_golf.dimensions = '3532x1754x1512'
muj_golf.manufacturer = 'volkswagen'
muj_golf.model = 'golf'
muj_golf.color = 'red'
muj_golf.year = 1991
muj_golf.engine = 1.6
muj_golf.fuel = 'gasoline'
muj_golf.performance = 55

muj_focus.color = 'red'
muj_focus.year = 2004
muj_focus.engine = 1.6
muj_focus.fuel = 'gasoline'
muj_focus.performance = 74

moje_octavia.color = 'blue'
moje_octavia.year = 2020
moje_octavia.engine = 1.5
moje_octavia.fuel = 'gasoline'
moje_octavia.performance = 110

# runtime
muj_golf.honk()
print('')
muj_golf.display()
print('')
muj_golf.steal()
print('')

muj_focus.honk()
print('')
muj_focus.display()
print('')
muj_focus.break_down()
print('')

moje_octavia.honk()
print('')
moje_octavia.display()
print('')
moje_octavia.ride()

# POLYMORPHISM
class Species:
    def intro(self):
        print("There are many types of beings")

    def flight(self):
        print('some can fly, some not.')

class Bird(Species):
    def flight(self):
        print('Birds usually fly, exceptions apply')
class Knife(Species):
    def flight(self):
        print('Knives usually do not fly, exceptions apply under certain condition')
class Shuttle(Species):
    def flight(self):
        print('Space shuttles used to fly a lot, sometimes in lot of pieces.')
# create instances
obj_Species = Species()
obj_Bird = Bird()
obj_knife = Knife()
obj_Shuttle = Shuttle()

obj_Species.intro()
obj_Species.flight()

obj_Bird.intro()
obj_Bird.flight()

obj_knife.intro()
obj_knife.flight()

obj_Shuttle.intro()
obj_Shuttle.flight()

# ENCAPSULATION

# DATA ABSTRACTIONS