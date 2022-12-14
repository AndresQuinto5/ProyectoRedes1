# Python-XMPP-Client
Minimal XMPP chat client-application made with python and SleekXMPP.

## Requirements

* Python 3.1+


## Installation guide

**Optional:** It's better if you try this in a python virtual enviroment.

1. Open files 
2. With you favorite terminal, access the folder containing the source code and install the dependencies with the command `pip install -r requirements.txt`
3. Run the main code with `python main.py`


## Features

This client provides basic features like sending messages, receiving messages and other essential chat-application stuff; all throughout a basic python CLI program.

* Register an account or login to an existing one.
* Show all users registered to the server & show your roster.
* Add a user to the roster/contact list.
* Get any user details (search).
* Send a private message to any user.
* Group chat options: NOT WORKING
  * Create a group.
  * Join an existing group.
  * Send a message to a group.
  * Leave a group you are part of.
* Send a presence message (define show and status).
* Send any file to a contact. NOT WORKING
* Log out of your account.
* Delete account from server.
* Send/Receive notifications


## How to

### File transfer (NOT WORKING, ONLY ON PY 37)

1. Select option 7 once you logged in.
2. Select the contact you want to send the file to.
3. If tkinter is installed, a file explorer will pop up in order for you to select a file. Otherwise, enter the path with regular slashes, like this example:

`C:/Users/User/Desktop/file.txt`

If you receive a file, it'll stored in the **received_files** folder with the name the user sent you.


## Notifications

There are several types of notifications, you'll receive them from the console with a format similar to this one: 

`|=================| NOTIFICATION TYPE |=================|`

The notifications you can get are:

* **NOW ONLINE:** When a user gets online.
* **MESSAGE** When a user sends you a message.
* **FILE TRANSFER** When a user requests a file transfer.
* **SUSCRIPTION** When a user subscribes to your presence or you subscribe to someone elses.
* **GROUPCHAT** When someone in a groupchat you're in changes its status or sends a message.

There are also other types of logs, but those are not interacting with another user directly or are not as important as the ones described.


## Useful notes

* In order to read any message that a user sent you, first you must "send a private message" or "send a message to a group" and then select the desired user/room. This will show you a list containing all the messages managed throughout the session (if any). You may then skip sending a message back by just pressing enter, without entering any text on the input.
* Installing the versions specified in **requirements.txt** is **HIGHLY RECOMMENDED** due to some bugs that SleekXMPP latest version contains. That's why it's recommended to set up a virtual enviroment.
* This project **DOES NOT** handle all of the errors from the server. Actually, some features might not work as desired with other created clients.
* This project was developed using **python 3.9.1**


## Main scripts

* **Main.py:** it's the main program. In this file, you interact with the console and the XMPP client indirectly.
* **client.py** "backend" file used for most of the implementation. Here you can find the Client class, which is used to manage all XMPP events, some prints and the main utility of the sleekXMPP library.
* **consts.py** Just contains some constants so that main code looks cleaner.


