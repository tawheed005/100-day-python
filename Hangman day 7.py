import random
stages =  ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
stages.reverse()

world_list = ['ant' , 'baboon' , 'badger' , 'bat', 'bear', 'beaver' ,'camel', 'cat', 'clam' ,'cobra' ,'cougar'
         ,'coyote' ,'crow' ,'deer', 'dog', 'donkey', 'duck' ,'eagle' ,'ferret', 'fox', 'frog' ,'goat' ,
         'goose', 'hawk' ,'lion', 'lizard', 'llama', 'mole', 'monkey' ,'moose' ,'mouse' ,'mule' ,'newt',
         'otter' ,'owl', 'panda', 'parrot' ,'pigeon' ,'python', 'rabbit' ,'ram' ,'rat' ,'raven'
         ,'rhino', 'salmon' ,'seal', 'shark' ,'sheep' ,'skunk', 'sloth', 'snake' ,'spider',
         'stork' ,'swan', 'tiger', 'toad' ,'trout' ,'turkey' ,'turtle', 'weasel' ,'whale' ,'wolf',
         'wombat' ,'zebra ']

computer_choice = random.choice(world_list)
welcome = ''' 
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█
'''

logo = ''' 
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
''' 
print(welcome, "\n" ,logo)

print(computer_choice)

number_of_letters = ""
length_word = len(computer_choice)
for position in range (length_word):
    number_of_letters += "_"
    
print(number_of_letters)

game_over = False
correct_guess = []
real_lives = 6
while not game_over:
    user_guess = input("guess a word: ").lower()
    if user_guess in correct_guess:
        print("you have already guessed :",{user_guess})

    display = ""
    for true_letters in computer_choice:
        if true_letters == user_guess:
            display += true_letters
            correct_guess .append(user_guess)
        elif true_letters in correct_guess:
            display += true_letters
        else:
            display += "_"
    if user_guess not in computer_choice:
        real_lives -= 1
        print("you entered",{user_guess},"its wrong ! you have lost a life")
        print("correct word was",{true_letters})
        if real_lives == 0 :
            game_over = True
            print("you lose")


    if "_" not in display:
        game_over = True
        print("you win")
    
    print("total lives = 6\nyour lives :",{real_lives} ,)
    print(display)
    print(stages[real_lives])



