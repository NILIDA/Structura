class Water:
    def __init__(self):
        self.isboiled = False

class Kettle:
    def __init__(self):
        self.water = None

    def isfull(self):
        if self.water is not None:
            return True
        return False

    def boil(self):
        if self.water is not None:
            self.water.isboiled = True
            print("It's boiled")
        else:
            print("No water")

    def removeWater(self):
        self.water = None
        print("It's removed")

    def fullIt(self, water):
        self.water = water

class Match:
    def __init__(self, matches):
        self.matches = matches

    def use_one(self):
        if self.matches > 0:
            self.matches -= 1
            return True
        return False

class Sink:
    def __init__(self, all_water):
        self.all_water = all_water
        self.kettle = None

    def putKettle(self, kettle):
        self.kettle = kettle

    def removeKettle(self):
        self.kettle = None

    def fullKettle(self):
        if self.all_water and not self.kettle.isfull():
            self.kettle.fullIt(self.all_water.pop())
            print("It's filled")
        else:
            print("No water")

class Cooker:
    def __init__(self, matches):
        self.matches = matches
        self.kettle = None

    def putKettle(self, kettle):
        self.kettle = kettle

    def removeKettle(self):
        self.kettle = None

    def boilKettle(self):
        if self.kettle and self.matches.use_one():
            self.kettle.boil()

my_match = Match(10)
my_kettle = Kettle()
the_water = [Water()]
my_sink = Sink(the_water)
my_sink.putKettle(my_kettle)
my_sink.fullKettle()
my_sink.removeKettle()
my_cooker = Cooker(my_match)
my_cooker.putKettle(my_kettle)
my_cooker.boilKettle()
my_cooker.removeKettle()
my_kettle.removeWater()