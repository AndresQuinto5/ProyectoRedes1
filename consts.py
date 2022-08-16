"""
Universidad del valle de Guatemala
Redes 1
Proyecto 1 chat con protocolo XMPP
AndresEmilioQuinto - 18288

"""


HEADER = '\033[95m'
OKBLUE = '\033[94m' + 'OK: '
OKGREEN = '\033[92m' + 'OK: '
WARNING = '\033[93m' + 'WARNING: '
FAIL = '\033[91m' + 'FAIL: '
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[1;30m'
BLUE = '\033[94m'
RED = '\033[91m'
YELLOW = '\033[93m'

# Menu messages
login_menu = f"""
{HEADER}|=================| LOGIN MENU |=================|{ENDC}
1. Register a new account
2. Log into an account
3. Exit
{HEADER}|================================================|{ENDC}
"""

main_menu = f"""
{HEADER}|=================| MAIN MENU |=================|{ENDC}
1. Show all connected users & my contact list
2. Add a user to my contact list
3. Show user details
4. Private chat
5. Group chat
6. Presence message
7. Send file
8. Log out
9. Delete my account
{HEADER}|===============================================|{ENDC}
"""
