import random
letters = ["a" , "b" , "c", "d" , "e", "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" ,  "v" , "w" , "x" , "y" , "z"]
numbers = ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
symbols = ["!" , "@" , "#" , "#" , "$" , "$" , "%" , "^" , "&" , "*" , "(" , ")"]


letter_input = int(input("welcome to td password generator \n How many letters do you want in the password: "))
number_input = int(input("How many numbers : "))
symbols_input = int(input("How many symbols : "))

password_list =[]
for character in range (1 , letter_input + 1)  :
    password_list.append (random.choice(letters))

for character in range (1 , number_input +1)  :
    password_list.append (random.choice(numbers))

for character in range (1 , symbols_input + 1)  :
    password_list.append (random.choice(symbols))

random.shuffle(password_list)
new_password = ""
for memo in password_list :
    new_password += memo
print (new_password)

    
     
  








