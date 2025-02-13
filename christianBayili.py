
import random

capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau',
                'Arizona':'Phoenix', 'Arkansas':'Little Rock',
                'California':'Sacramento', 'Colorado':'Denver',
                'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta',
                'Hawaii':'Honolulu', 'Idaho':'Boise',
                'Illinois':'Springfield', 'Indiana':'Indianapolis',
                'Iowa':'Des Moines', 'Kansas':'Topeka',
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
                'Maine':'Augusta', 'Maryland':'Annapolis',
                'Massachusetts':'Boston', 'Michigan':'Lansing',
                'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
                'Missouri':'Jefferson City', 'Montana':'Helena',
                'Nebraska':'Lincoln', 'Nevada':'Carson City',
                'New Hampshire':'Concord', 'New Jersey':'Trenton',
                'New Mexico':'Santa Fe', 'New York':'Albany',
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
                'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
                'Rhode Island':'Providence', 'South Carolina':'Columbia',
                'South Dakota':'Pierre', 'Tennessee':'Nashville',
                'Texas':'Austin', 'Utah':'Salt Lake City',
                'Vermont':'Montpelier', 'Virginia':'Richmond',
                'Washington':'Olympia', 'West Virginia':'Charleston',
                'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

correct = incorrect = 0    

#Get list of all states
states = list(capitals.keys())

while True:
    # Select Random State
    current_state = random.choice(states)
    
    user_solution = input(f'\nWhat is the capital of {current_state}? (or enter Q to quit): ')
    if user_solution == 'Q' or user_solution == 'q':
        break
    if user_solution.lower() == capitals[current_state].lower():
        print('You are Correct!')
        correct += 1
    else:
        print("You are Incorrect!")
        incorrect += 1
    
    #Remove recently asked state from list
    states.remove(current_state)
    
    if len(states) == 0:
        print("You have completed the Game!")
        break
        

print("\nHere are your Scores")

print(f"Correct Answers : {correct}")
print(f"Incorrect Answer : {incorrect}")

if correct > 0:
    print(f"\n Your Final Score is : {correct} / {correct + incorrect} = {(correct*100) / (correct + incorrect)}")
else:
    print(f"\n Your Final Score is : 0")