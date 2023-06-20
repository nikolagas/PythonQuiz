import random
from questions import questions_dic
from string import ascii_lowercase


quiz_length = '10'
players = []

print('I welcome you to this Science Quiz')


def run_quiz():
    user_name = input('Enter your name: ')
    while not user_name.isalpha():
        print('Invalid name - please enter alphabetical characters only')
        user_name = input('Try again: ')
    print(f'Hello, {user_name}, please choose your quiz length below.')

    while True:
        global quiz_length
        quiz_length = input('You quiz can be 10, 15 or 20 questions. Choose: ')
        if quiz_length == '10' or quiz_length == '15' or quiz_length == '20':
            break
        else:
            print('Invalid option. Try again')
            continue

    # A function to read and randomise the order of questions
    questions = read_questions()
    
    # A variable to keep track of the user's score
    num_correct = 0

    for num, (question, answers) in enumerate(questions, start=1): 
        print(f"\nQuestion {num}:")
        
        num_correct += ask_question(question, answers)

    print(f'\n{user_name}, you scored {num_correct} correct out of {num} questions')
    print(f'\nPercentage score: {get_percentage_score(num_correct, int(quiz_length))}')

    players.append(Player(user_name, num_correct, quiz_length))
    
    add_new_player()


def read_questions():
    number_of_questions = min(int(quiz_length), len(questions_dic))
    return random.sample(list(questions_dic.items()), k=number_of_questions)


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


def get_answer(question, answers):
    print(f"{question}?")
    labeled_answers = dict(zip(ascii_lowercase, answers))
    for label, answer in labeled_answers.items():
        print(f"  {label}) {answer}")

    while (answer_label := input("\nYour answer? ")) not in labeled_answers:
        print(f'Please answer one of a, b, c or d')

    return labeled_answers[answer_label]


def add_new_player():
    while True:
        try:
            new_player = input(f'\nAnyone else want to play? Yes or No: ')
            if new_player in ['Y', 'Yes', 'y', 'yes']:
                run_quiz()
                break
            elif new_player in ['N', 'No', 'n', 'no']:
                print('\nIndividual results are presented below')
                for player in players:
                    print(f'[ {player.name}: {player.score} / {player.total_questions}: '
                          f'{get_percentage_score(player.score, int(player.total_questions))}% ]')
                print(f'Highest total score: {max_total_score()}'
                      f'\nHighest percentage score: {max_percentage_score()}')
                break
        except ValueError:
            print('Choose yes or no.')
            continue
    return new_player


def get_percentage_score(score, total):
    return round(score / total * 100)


def max_total_score():
    return max(players, key=lambda player: player.score)


def max_percentage_score():
    return max(players, key=lambda player: player.score / int(player.total_questions * 100))


class Player:
    def __init__(self, name, score, total_questions):
        self.name = name
        self.score = score
        self.total_questions = total_questions

    def __repr__(self):
        return f'{self.name}: {self.score} / {self.total_questions}: {get_percentage_score(self.score, int(self.total_questions))}% '


run_quiz()
