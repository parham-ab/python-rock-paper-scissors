import random

# all choices
choices = ['rock', 'paper', 'scissors']

while True:
    computer_choice = choices[random.randint(0, len(choices) - 1)]
    user_choice = input('Rock, Paper, scissors...').lower()
    print('Computer: ' + computer_choice)
    print('User: ' + user_choice)

    while user_choice not in choices:
        print('Invalid choice!')
        user_choice = input('Rock, Paper, scissors...').lower()

    if computer_choice == 'rock':
        if user_choice == 'rock':
            print('equal')
        elif user_choice == 'paper':
            print('you win!')
        elif user_choice == 'scissors':
            print('you loose!')

    if computer_choice == 'paper':
        if user_choice == 'paper':
            print('equal')
        elif user_choice == 'rock':
            print('you loose!')
        elif user_choice == 'scissors':
            print('you wind!')

    if computer_choice == 'scissors':
        if user_choice == 'scissors':
            print('equal')
        elif user_choice == 'rock':
            print('you win!')
        elif user_choice == 'paper':
            print('you loose!')

    play_again = input('Play Again? Y / N').lower()
    if play_again != 'Y'.lower():
        break

print('Have a Good Time 😉!')
