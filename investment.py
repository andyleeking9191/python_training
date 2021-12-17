# Challenge: Create a simple program that calculates your investment total. 
# Your initial investment is $0.01. Your investment doubles every day 
# and will be invested for a total of 30 days. 

investment = .01
investment_days = 30

for i in range(investment_days):
    investment *= 2

print(investment)