"""
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
first_name = first_name.capitalize()
last_name = last_name.capitalize()
print("Your name is ", first_name, last_name )

#refactored
a = int(input("Enter a number: ")) # a = input("Enter a number: ") + a = int(a)
b = int(input("Enter another number to be added to the first: ")) # b = input("Enter another number to be added to the first: ") + b = int(b)

print("The sum of these numbers is "+ str(a + b))
"""
""" 
first_num = int(input("Choose 1st number: "))
second_num = int(input("Choose 2nd number: "))
choose_operator = input("Choose operator: ")
if second_num > first_num and choose_operator == "-" :
    print(second_num - first_num) 
elif first_num == second_num and choose_operator == "-":
    print(first_num - second_num)
elif first_num > second_num and choose_operator == "-":
    print("Negative values are not allowed")
elif choose_operator == "+":
    print(first_num + second_num)
else:
    print("Not expected operation")
"""
# for loops
#test_scores = [45, 23, 89, 78, 98, 55, 74, 87, 95, 75]
#test_scores.sort(reverse = True)
#for i in range(0, 3, 1):
#    print(test_scores[i])
"""
for number_range in range(10, 60, 10):
    if number_range > 50:
        print("And we're done!")
        continue
    print(number_range)

# while loop
number_range = 10
while number_range < 60:
    print(number_range)
    number_range += 10
if number_range > 50:
    print("And we're done!")
"""    