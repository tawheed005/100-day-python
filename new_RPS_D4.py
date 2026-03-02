import random
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n Rock""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
\n Paper""")

scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\n Scissors""")

art = [rock,paper,scissor]
choice_1 = int(input("Enter : 0 for rock, 1 for paper , 2 for sicssor : "))
randomizer = random.randint(a=0,b=2)

print("you choose : ", art [choice_1])
print("computer choose :",art [randomizer])

if choice_1 == randomizer :
    print ( "draw" )
elif choice_1 == 1 and randomizer == 0 :
    print("you won")
elif choice_1 == 2 and randomizer == 1:
    print("you won")
elif choice_1 == 0 and randomizer == 2:
    print("you won")
else:
    print( "you lose")

        


            

