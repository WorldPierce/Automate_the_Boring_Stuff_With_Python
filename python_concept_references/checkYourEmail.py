import imapclient, pyzmail # internt mail accesable protocol
conn = imapclient.IMAPClient('imap.gamil.com', ssl=True)
conn.login('email@gmail.com', 'password')
conn.select_folder('INBOX', readonly=True)

UIDS = conn.search(['SINCE 20-Aug-2016']) # returns list
# UIDVAL represents an entry in the UIDS list
rawMessageconn.fetch([UIDVAL], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[UIDVAL][b'BODY[]'])

message.getSubject() # returns subject text
message.get_address('from') # or 'to' 'bcc'

# to get text values in body
message.text_part.get_payload().decode('UTF-8')

conn.list_folders() # returns list of all folders

# to delete emails
conn.select_folder('INBOX', readonly=False)

UIDS = conn.search(['ON 24-Feb-2017'])
conn.delete_messages(UIDS)


conn.logout()
