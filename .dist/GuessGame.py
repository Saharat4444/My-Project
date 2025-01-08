from random import randint

answer = randint(1, 10)

while True:
    try:
        guess = int(input('Guess a number 1-10: '))
        if 0 < guess < 11:
            if guess == answer:
                print('The answer is correct!')
                break
            else:
                print('Try again!')
        else:
            print("Hey, it's only 1-10!")
    except ValueError:
        print('Please enter a number.')
