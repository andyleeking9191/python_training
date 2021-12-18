# The comfortable relative humidity for humans is between 40% and 60%.
# The given program takes the percent of humidity as input. 
# Complete the code to output "norm" if the taken percent of humidity is in the range of 40 and 60. 
# Otherwise output "not norm".

humidity = int(input("Enter the current humidity percentage: "))

if humidity >= 40 and humidity <= 60:
    print("norm")
else:
    print("not norm")