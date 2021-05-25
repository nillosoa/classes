import random, logging

logging.basicConfig(filename='debugging-coin-toss.txt', level=logging.DEBUG, format='%(levelname)s: %(message)s')
logging.info('This is a fixed script from \'Automate the Boring Stuff with Python\'\'s Chapter 10.')
logging.info('Starting game: debugging-coin-toss.py')
logging.info('Start time: %(asctime)s')

toss = random.randint(0, 2) # 0 is tails, 1 is heads
if toss == 0:
    toss = 'tails'
    logging.debug('tossed 0(tails)')
elif toss == 1:
    toss = 'heads'
    logging.debug('tossed 1(heads)')

# reusing code? better put it in a function
def askGuess():
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    return guess

# now a 'for' loop for reptition...
for guesses in range(2):
    guess = askGuess()
    if guess == toss:
        print('You got it!')
        logging.info('Right guess! breaking the loop.')
        break
    else:
        print('Nope. You are really bad at this game.')
        if guesses == 0:
            print('This is your last chance. Try again.')
            logging.debug('Wrong guess. Starting second loop.')
        else:
            logging.info('Wrong guess. User ran out of guesses.')

logging.debug("End of script.\n")


       