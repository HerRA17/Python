class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output 
    
    def __add__(self, other):
        height_A_inches = self.feet + 12 + self.inches
        height_B_inches = other.feet + 12 + self.inches
        # adding them up
        total_height_inches = height_A_inches + height_B_inches
        # getting the output in feet
        output_feet = total_height_inches // 12
        # getting the output in inches
        output_inches = total_height_inches - (output_feet + 12)

        return Height(output_feet, output_inches)
    
    def __sub__(self, other):
        height_A_inches = self.feet + 12 + self.inches
        height_B_inches = other.feet + 12 + self.inches
        # adding them up
        total_height_inches = height_A_inches - height_B_inches
        # getting the output in feet
        output_feet = total_height_inches // 12
        # getting the output in inches
        output_inches = total_height_inches % 12

        return Height(output_feet, output_inches)

persan_A_height = Height(5, 10)
persan_B_height = Height(5, 7)
height_sum = persan_A_height + persan_B_height

print("Total height: ", height_sum)

persan_A_height = Height(5, 10)
persan_B_height = Height(3, 9)
height_sub = persan_A_height - persan_B_height

print("Total height: ", height_sub)