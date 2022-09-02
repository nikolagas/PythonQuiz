import random
from string import ascii_lowercase

questions_dic = {
    'When was the idea of the atom first introduced': [
        '450 B.C.',
        '1050',
        '1791',
        '1942',
    ],

    'What planet has the most moons': [
        'Saturn',
        'Neptune',
        'Uranus',
        'Jupiter',
    ],

    'Where are the three smallest bones in the human body': [
        'Middle Ear',
        'Nose',
        'Toes',
        'Eyes',
    ],

    'What hormone does the pancreas produce': [
        'Insulin',
        'Estrogen',
        'Adrenaline',
        'Testosterone',
    ],

    'What is Johannes Kepler best known for': [
        'Laws of planetary motion',
        'Laws of gravity',
        'Laws of thermodynamics',
        'Laws of motion',
    ],

    'Which of the following evolved first': [
        'Sharks',
        'Humans',
        'Trees',
        'Cockroaches',
    ],

    'CH3COOH is the chemical formula for what common household item': [
        'Vinegar',
        'Table salt',
        'Ammonia',
        'Hand soap',
    ],

    'What discovery earned Wilhelm Roentgen the first Nobel Prize for Physics': [
        'X-rays',
        'Wireless telegraphy',
        'Radioactivity',
        'The neutron'
    ],

    'What is the smallest biological unit of a living organism': [
        'Cell',
        'Molecule',
        'Atom',
        'Tissue',
    ],

    'Which of the following is NOT generally considered a greenhouse gas': [
        'Oxygen',
        'Carbone dioxide',
        'Ozone',
        'Water vapor'
    ],

    'In which type of chemical bonding are electrons shared between adjacent atoms': [
        'Covalent',
        'Isotopic',
        'Ionic',
        'Subatomic',
    ],

    'If one inch of rain was turned to snow, how much snow would you have': [
        '10 inches',
        '1 inch',
        '2 inch',
        '1/2 inch',
    ],

    'Which of the following has the most neck vertebrae': [
        'All have the same',
        'Human',
        'Giraffe',
        'Mouse',
    ],

    'Who wrote the first algorithm intended to be carried out by a machine': [
        'Ada Lovelace',
        'Alan Turing',
        'Marvin Minsky',
        'Claude Shannon',
    ],

    'When was the first fax machine invented': [
        '1840s',
        '1930s',
        '1870s',
        '1980s',
    ],

    'What is the standard unit of kinetic energy': [
        'Joule',
        'Newton',
        'Calorie',
        'Watt',
    ],

    'What do you call an interstellar cloud of dust': [
        'Nebula',
        'Parsec',
        'Ionosphere',
        'Penumbra',
    ],

    'How many chambers does the human heart have': [
        '4',
        '3',
        '1',
        '2',
    ],

    'What temperature is absolute zero': [
        '-273 Celsius',
        '-333 Celsius',
        '0 Celsius',
        '-459 Celsius',
    ],

    'What species of reptile is the sole surviving member of its order': [
        'Tuatara',
        'Crocodile',
        'Caecilian',
        'Terrapin',
    ]

}

quiz_length = '10'
players = []

print('I welcome you to this Science Quiz')


def run_quiz():
    # Asks the user for their name
    user_name = input('Enter your name: ')
    while not user_name.isalpha():
        print('Invalid name - please enter alphabetical characters only')
        user_name = input('Try again: ')
    print(f'Hello, {user_name}, please choose your quiz length below.')

    # Asks the user for their preferred quiz length
    while True:
        global quiz_length
        quiz_length = input('You quiz can be 10, 15 or 20 questions. Choose: ')
        if quiz_length == '10' or quiz_length == '15' or quiz_length == '20':
            break
        else:
            print('Invalid option. Try again')
            continue

    # A function to randomise the number of questions the user specifies
    questions = read_questions()
    # A variable to keep track of the user's score
    num_correct = 0

    for num, (question, answers) in enumerate(questions, start=1):  # Enumerates the questions starting from 1
        print(f"\nQuestion {num}:")

        # Keeping track of users' scores is done by the ask_question function
        num_correct += ask_question(question, answers)

    # Prints the users correct questions and percentage scores
    print(f'\n{user_name}, you scored {num_correct} correct out of {num} questions')
    print(f'\nPercentage score: {get_percentage_score(num_correct, int(quiz_length))}')

    # Adds every individual player to a list of players
    players.append(Player(user_name, num_correct, quiz_length))
    # Function to prompt for new player, validate input, run quiz again if needed and print scores of players
    add_new_player()


# Function to randomise the questions for the chosen quiz length
def read_questions():
    number_of_questions = min(int(quiz_length), len(questions_dic))
    return random.sample(list(questions_dic.items()), k=number_of_questions)


# Function to randomise the answer options and check for correct answer
def ask_question(question, answers):
    correct_answer = answers[0]  # Correct answer is always the first item in the list of answers
    labeled_answers = random.sample(answers, k=len(answers))  # Randomises answer options

    answer = get_answer(question, labeled_answers)
    if answer == correct_answer:
        print('That is correct. You scored a point!')
        return 1
    else:
        print(f"Incorrect. It's {correct_answer}, not {answer}")
        return 0


# Function to print the question, answers and validate user choice: a, b, c or d
def get_answer(question, answers):
    print(f"{question}?")
    labeled_answers = dict(zip(ascii_lowercase, answers))
    for label, answer in labeled_answers.items():
        print(f"  {label}) {answer}")

    while (answer_label := input("\nYour answer? ")) not in labeled_answers:
        print(f'Please answer one of a, b, c or d')

    return labeled_answers[answer_label]


# Optionally adds new player after the quiz is finished
def add_new_player():
    while True:
        try:
            new_player = input(f'\nAnyone else want to play? Yes or No: ')
            # If new player wants to play, main function is executed
            if new_player in ['Y', 'Yes', 'y', 'yes']:
                run_quiz()
                break
            # If not, player results are printed
            elif new_player in ['N', 'No', 'n', 'no']:
                print('\nIndividual results are presented below')
                for player in players:
                    print(f'[ {player.name}: {player.score} / {player.total_questions}: '
                          f'{get_percentage_score(player.score, int(player.total_questions))}% ]')
                break
        except ValueError:
            print('Choose yes or no.')
            continue
    return new_player


# Calculates percentage score
def get_percentage_score(score, total):
    return round(score / total * 100)


# Player class with three attributes: name, score and total questions (quiz length)
class Player:
    def __init__(self, name, score, total_questions):
        self.name = name
        self.score = score
        self.total_questions = total_questions


run_quiz()
