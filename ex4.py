# initialize cars to 100
cars = 100
# initialize space_in_a_car to 4.0 is used over 4 to return a floating point value when used with another integer primitive.
space_in_a_car = 4.0
# initialize drivers to 30
drivers = 30
# initialize passengers to 90
passengers = 90
# initialize cars_not_driven to cars (100) - drivers (30) = 70
cars_not_driven = cars - drivers
# initialize cars_driven to drivers = 30
cars_driven = drivers
# initialize carpool_capacity to cars_driven (30) * space_in_a_car (4.0) = 120.0
carpool_capacity = cars_driven * space_in_a_car
# initialize average_passengers_per_car to passengers (90) / cars_driven (30) = 3.0
# In Python 3, / is float division
# In Python 2, / is integer division (assuming int inputs)
# In both 2 and 3, // is integer division
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# <----- Explain what happened below ------>
# Traceback (most recent call last):
#  File "ex4.py", line 29, in <module>
#    average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# Python made a call to run a file on line 27. The file was ex4.py on line 28,
# python shows the location (line 29) of the error. On line 29 a variable
# average_passengers_per_car is initialized to car_pool_capacity / passenger
# car_pool_capacity was not created this was a syntax error the variable
# carpool_capacity should have been used.
# Line 30 explains what the error was and why it occurred.
