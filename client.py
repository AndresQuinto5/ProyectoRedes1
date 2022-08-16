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


DIRNAME = os.path.dirname(__file__)


class Client(ClientXMPP):

    def __init__(self, jid, password):

        ClientXMPP.__init__(self, jid, password)
        self.auto_authorize = True
        self.auto_subscribe = True
        self.contact_dict = {}
        self.user_dict = {}
        self.room_dict = {}
        self.file_received = ''

        # self.add_event_handler('session_start', self.session_start)
        self.add_event_handler('message', self.received_message)
        self.add_event_handler('disconnected', self.got_disconnected)
        self.add_event_handler('failed_auth', self.on_failed_auth)
        self.add_event_handler('presence_subscribed',
                               self.new_presence_subscribed)
        self.add_event_handler("got_offline", self.presence_offline)
        self.add_event_handler("got_online", self.presence_online)
        self.add_event_handler('changed_status', self.wait_for_presences)
        self.add_event_handler('groupchat_presence',
                               self.on_groupchat_presence)

        # FILE TRANSFER
        self.add_event_handler('si_request', self.on_si_request)
        self.add_event_handler('ibb_stream_start', self.on_stream_start)
        self.add_event_handler("ibb_stream_data", self.stream_data)
        self.add_event_handler("ibb_stream_end", self.stream_closed)

        self.register_plugin('xep_0030')
        self.register_plugin('xep_0004')
        self.register_plugin('xep_0066')
        self.register_plugin('xep_0077')
        self.register_plugin('xep_0050')
        self.register_plugin('xep_0047')
        self.register_plugin('xep_0231')
        self.register_plugin('xep_0045')
        self.register_plugin('xep_0095')  # Offer and accept a file transfer
        self.register_plugin('xep_0096')  # Request file transfer intermediate
        self.register_plugin('xep_0047')  # Bytestreams

        self['xep_0077'].force_registration = True

        self.received = set()
        self.presences_received = threading.Event()

    def session_start(self):
        try:
            self.get_roster(block=True)
        except IqError as err:
            print('Error: %s' % err.iq['error']['condition'])
        except IqTimeout:
            print('Error: Request timed out')

        self.send_presence()

    # Create a new user dict
    def create_user_dict(self, wait=False):

        try:
            self.get_roster(block=True)
        except IqError as err:
            print('Error: %s' % err.iq['error']['condition'])
        except IqTimeout:
            print('Error: Request timed out')

        groups = self.client_roster.groups()
        for jid in groups['']:
            # Check we are not evaluating ourselves or a conference room
            if jid == self.boundjid.bare or 'conference' in jid:
                continue

            # Get some data
            sub = self.client_roster[jid]['subscription']
            name = self.client_roster[jid]['name']
            username = str(jid.split('@')[0])
            connections = self.client_roster.presence(jid)

            # Check if connections is empty
            if connections.items():
                # Go through each connection
                for res, pres in connections.items():

                    show = 'available'
                    status = ''
                    if pres['show']:
                        show = pres['show']
                    if pres['status']:
                        status = pres['status']

                    # Check if the user is in the dict, else add it
                    if not jid in self.contact_dict:
                        self.contact_dict[jid] = User(
                            jid, name, show, status, sub, username, res)
                    else:
                        self.contact_dict[jid].update_data(
                            status, show, res, sub)

            # User is not connected, still add him to the dict
            else:
                self.contact_dict[jid] = User(
                    jid, name, 'unavailable', '', sub, username, '')
