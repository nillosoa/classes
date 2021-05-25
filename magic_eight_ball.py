#Magic 8-Ball answers by wikipedia(https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers)
from colorama import init, Fore, Style
from time import sleep
import random


affirmative = [
    "It is certain.", "It is decidedly so.", "Without a doubt.",
    "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."
]

negative = [
    "Don't count on it.", "My reply is no.",
    "My sources say no.", "Outlook not so good.",
    "Very doubtful."
]

non_committal = [
    "Reply hazy, try again.", "Ask again later.",
    "Better not tell you now.", "Cannot predict now.",
    "Concentrate and ask again."
]

answers = affirmative + non_committal + negative

init()
while True:
    input("Think of a question, then press enter.")

    #Drama club
    sleep(1)
    i = random.randint(0, len(answers) - 1)

    #Let's add some colors
    if answers[i] in affirmative: print(Fore.GREEN + answers[i])
    elif answers[i] in non_committal: print(Fore.YELLOW + answers[i])
    elif answers[i] in negative: print(Fore.RED + answers[i])

    print(Style.RESET_ALL)
