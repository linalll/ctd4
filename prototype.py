import random
guess_times = 0
bag = 0

guessed_numbers = []
print('this is a game, guess from 1-5 balls ')
while guess_times < 1:              #while loop
    num = input('enter a number :')
    guessed_numbers.append(num)
    guess_times += 1

print(guessed_numbers)


print(' guess from 1-3 bag ')
bag= int (input('enter a bag number :'))


if bag < 1:

    bagnumber = []
    random_num = random.randrange(1, 5)
    bagnumber.append(random_num)
    print(bagnumber)

if bag <2:
    bagnumber = []
    random_num = random.randrange(1, 5)
    bagnumber.append(random_num)
    print(bagnumber)


if bag < 3:
    bagnumber = []
    random_num = random.randrange(1, 5)
    bagnumber.append(random_num)
    print(bagnumber)


correct_guess = []
 
for num in guessed_numbers:
  
    if num in bagnumber == num in guessed_numbers:
        correct_guess.append(num)

print('your correct guesses  are', correct_guess)
print('you guessed ', guessed_numbers)
print('the supposed are ', bagnumber)