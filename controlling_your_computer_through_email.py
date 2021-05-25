# controlling_your_computer_through_email.py - verify an account for new emails
# in the inbox folder with the subjective 'CYCTE' and for each link in the email
# body, opens a browser tab.
# The original project downloads bitorrent links, but I've adapted to open links
# instead of torrent files


import imapclient, webbrowser, email, time, re
import sys, logging

WAIT = 60 * 15 # How long to wait before a new connection(in seconds).
KEYWORD = u'CYCTE' # What to look for on emails
LINKREG = re.compile(r'((http(s)?:\/\/)([a-z0-9\.]+)(.*))')

CONFIG = {
    'HOST': 'imap.gmail.com',
    'PORT': 993,
    'EADDRESS': 'd.cyanide07@gmail.com',
    'PASSWORD': 'a^9*HBLXcRy8p$I'
}

logging.basicConfig(filename='cycte.log.txt', format='%(message)s - %(asctime)-15s')
logger = logging.getLogger('cycte')
logger.setLevel(logging.DEBUG)
while True:
    conn = imapclient.IMAPClient(CONFIG['HOST'], CONFIG['PORT'], ssl=True)
    conn.login(CONFIG['EADDRESS'], CONFIG['PASSWORD'])
    logger.debug('Connected to %s:%d with %s.' %(CONFIG['HOST'], CONFIG['PORT'], CONFIG['EADDRESS']))

    if not conn.folder_exists('executed'):
        logger.debug('Creating folder \'executed\'.')
        conn.create_folder('executed')

    conn.select_folder('INBOX')

    UIDs = conn.search([u'SUBJECT', KEYWORD])
    logger.debug('Found %d %s new messages.' %(len(UIDs), KEYWORD))
    for uid, data in conn.fetch(UIDs, ['BODY[]', 'FLAGS']).items():
        message = email.message_from_bytes(data[b'BODY[]'])
        payload = message.get_payload()

        if payload == None:
            logger.debug('Found empty payload UID %d.' %uid)
            continue
        
        if message.is_multipart():
            payload = payload[0].as_string()

        for group in LINKREG.findall(payload):
            logger.debug('Opening default browser for %s.' %group[0])
            webbrowser.open(group[0])
        
        conn.move([uid], 'executed')
        logger.debug('Moving - uid %s - to executed folder.' %uid)
        logger.debug('Done.')
    time.sleep(WAIT)