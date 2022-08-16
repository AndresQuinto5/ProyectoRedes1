"""
Universidad del valle de Guatemala
Redes 1
Proyecto 1 chat con protocolo XMPP
AndresEmilioQuinto - 18288

"""

import os
import logging
import time
import sleekxmpp
from getpass import getpass
from prettytable import PrettyTable
from sleekxmpp.exceptions import IqError, IqTimeout

import client
from consts import *

close_login = False

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(levelname)-8s %(message)s')


# With tkinter, opens a windows for the user to select a file.
def get_file_path():
    file_path = filedialog.askopenfilename()
    return file_path
