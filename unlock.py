#
# Copyright 2019 (C) Wiggy boy <Lindholm>
# (formally known as Osvald Lindholm)
#

import time, os
from threading import Thread
from keyring import get_credential as get_keyring_credential

# Type your password here
#
# Warning! Your password will now be stored in plain text. That
# is any program can read this file and your system is thus very
# insecure. Make sure you take other security measures to insure
# the safety of your system.
password = ""


# Triggers the keyring popup if the keyring is not unlocked already.
# Locks the thread until the popup is closed.
#
# The credentials requested are arbitrary, they are not of interest.
def trigger_keyring_unlock_popup():
    get_keyring_credential("service", "login")


# Create a thread to trigger the keyring unlock popup.
popup = Thread(target = trigger_keyring_unlock_popup)
popup.start()

def is_locked(): return popup.is_alive()

# Wait a moment for the system to react
# Then check if the system is locked or not
time.sleep(0.1)
if (is_locked()):
    if (password == ""):
        print("The system is locked and a unlock popup has been triggered!")
    else:
        os.system("xdotool type " + password)
        os.system("xdotool key Return")

        time.sleep(0.1)
        if (is_locked()):
            print("Unlock unsuccessful, incorrect password!")
