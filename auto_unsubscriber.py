#! python3
# auto_unsubscriber.py - Look for unsubscribe links in a email ac and
# automatically opens it in a webbrowser.
# Use: auto_unsubscriber.py [server]
# services outlook, gmail


import imapclient, webbrowser, bs4, sys
import email as email_parser
import re


services = {
    'outlook': ['imap-mail.outlook.com', 993],
    'gmail':   ['imap.gmail.com', 993]
}

if len(sys.argv[1:]) < 1:
    print('Missing arguments.')
    print('Use: python %s [service]' %sys.argv[0])
    sys.exit()

service = sys.argv[1]

if not service.lower() in services.keys():
    print('SMTP server not in services list.')
    print('These are the supported services: ' + ', '.join(services.keys()))
    sys.exit()

email = None
email_regex = re.compile(r'((.*)@(.*).([a-z.]))')
if len(sys.argv[1:]) < 2:
    while email == None:
        inputed = input('Account email: ')
        if email_regex.search(inputed):
            email = inputed
else:
    email = sys.argv[2]


if len(sys.argv[1:]) < 3:
    for i in range(4):
        if i < 3:
            password = input('Account password: ')
            if not password == '':
                break
        else:
            print('Exhausted.')
            sys.exit()
else:
    password = sys.argv[3]

server_name = services[service][0]
server_port = services[service][1]
imapObj = imapclient.IMAPClient(server_name, port=server_port)
imapObj.login(email, password)
imapObj.select_folder('INBOX', readonly=True)

UIDs = imapObj.search([u'ALL'])
TOTAL_EMAILS = len(UIDs)

raw_messages = imapObj.fetch(UIDs, ['BODY[]', 'FLAGS']) 
unsubscribed = []
for msgid, data in raw_messages.items():
    message = email_parser.message_from_bytes(data[b'BODY[]'])
    message_from    = message['From']
    message_subject = message['Subject']

    if message_from in unsubscribed:
        continue

    payload = message.get_payload(decode=True)
    if payload == None:
        continue

    soup = bs4.BeautifulSoup(payload, 'html.parser')
    for a in soup.find_all('a'):
        if 'href' in a.attrs:
            if ('unsubscribe' in a.text.lower()) or ('unsubscribe' in a['href']):
                print('"%s" from %s may be a subscription; Following found url %s.' %(message_subject, message_from, a['href']))
                webbrowser.open(a['href'])
                unsubscribed.append(message_from)


print('Unsucribed from %d newsletters.' %len(unsubscribed))
print('Exhausted.')