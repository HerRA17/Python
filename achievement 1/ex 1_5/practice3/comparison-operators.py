class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __ge__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A >= height_inches_B

    def __ne__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A != height_inches_B

    def __gt__(self, other):
        height_inches_A = self.feet * 12 + self.inches
        height_inches_B = other.feet * 12 + other.inches
        return height_inches_A > height_inches_B

height1 = Height(4, 6)
height2 = Height(4, 5)
height3 = Height(4, 6)

print(height1 > height2)
print(height1 >= height3)
print(height2 != height1)