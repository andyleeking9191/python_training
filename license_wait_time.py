# Challenge: 
# You have to get a new driver's license and you show up at the office at the same time as 4 other people. 
# The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. 
# All of the agents are available now, and they can each see one customer at a time. 
# How long will it take for you to walk out of the office with your new license?

def new_license_wait_time():
    your_name = input('Enter your name: ')
    num_agents = int(input('Enter the number of agents working: '))
    names_list = list(input('Enter the names of the other people in line: ').split())

    names_list.append(your_name)
    names_list.sort()

    num_in_line = names_list.index(your_name) + 1

    if num_in_line <= num_agents:
        print(f'{your_name} it will take you 20 minutes to get your license.')
    else:
        print(f'{your_name} it will take you '+ str((num_in_line - num_agents) * 20 + 20) + ' minutes to get your license.')

new_license_wait_time()        

