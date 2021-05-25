#! python3
# random_chore_emailer.py - Assigns and emails people random chores


import random, smtplib, pprint


myEmail = 'd.cyanide07@gmail.com'
myPassword = 'a^9*HBLXcRy8p$I'
People = {
    'Charlie': 'charlie@example.com',
    'Alice': 'alice@example.com',
    'Bob': 'bob@example.com',
    'Ted': 'ted@example.com'
    }
Chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

smtpObj.login(myEmail, myPassword)

for person, email in People.items():
    chore = random.choice(Chores)
    Chores.remove(chore) # Removes the chore so it won't get repeated

    message = 'Subject: Chores\nHello, %s\nThe following chore was assigned to you: %s.' %(person, chore)
    try:
        smtpObj.sendmail(myEmail, myEmail, message) # emailing myself.
        print('Email suscefully sent to %s at %s with %s chore.' %(person, email, chore))
    except Exception as e:
        print('Could not email chore %s to %s at %s:' %(chore, person, email))
        pprint.pprint(e)

smtpObj.quit()
print('Done.')