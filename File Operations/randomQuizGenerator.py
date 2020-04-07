#Creates quizzes with questions and answers in a random order, along with the answer key

import random, os
from pathlib import Path

# Quiz data based on states
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Make a sub directory path for the quiz files
path = Path.cwd() / Path('File Operations/Quiz Files')

#If the folder doesn't exist then make it
if path.exists() == False:
     #Make the sub directory
    Path(path).mkdir()

# Change the cwd to the sub folder
os.chdir(path)

for quizNum in range(35):
    # Create the quiz and answer key files
    quizFile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt', 'w')

    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    #Shuffle state order
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        # Gets correct answer by pulling a state from the shuffled list then finding the value in the un shuffled capitals list
        correctAnswer = capitals[states[questionNum]]
        # Gets the wrong answer by copying the answer list and removing the correct answer
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # Creates the options by getting a random slice of the list and adding the correct value to it 
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        # Shuffle the answer options list
        random.shuffle(answerOptions)

        # Write quiz and answer options to the file
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            # The below treats 'ABCD' as an aray so this will loop though and write A then B etc
            quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}\n")
        
        quizFile.write('\n')
        # This will write the correct answer to the answer file by finding the correct index for the answer in the answer options
        # and writing the relvent ABCD letter to the file for that question number
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
        answerKeyFile.write('\n')
    
    # Close off the text files
    quizFile.close()
    answerKeyFile.close()