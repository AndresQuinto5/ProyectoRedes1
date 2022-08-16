"""
Universidad del valle de Guatemala
Redes 1
Proyecto 1 chat con protocolo XMPP
AndresEmilioQuinto - 18288

"""

import os
import time
import logging
import getpass
import threading
import base64
import datetime
import mimetypes
from sleekxmpp import ClientXMPP
from sleekxmpp.exceptions import IqError, IqTimeout
from xml.etree import cElementTree as ET
from sleekxmpp.plugins.xep_0004.stanza.field import FormField, FieldOption
from sleekxmpp.plugins.xep_0004.stanza.form import Form
from sleekxmpp.plugins.xep_0047.stream import IBBytestream
from consts import OKGREEN, OKBLUE, WARNING, FAIL, ENDC, BLUE, RED, NEW_MESSAGE, FILE_OFFER, SUSCRIPTION, GOT_ONLINE, error_msg, GROUPCHAT, STREAM_TRANSFER

