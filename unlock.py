#
# Copyright 2019 (C) Wiggy boy <Lindholm>
# (formally known as Osvald Lindholm)
#

import time
from threading import Thread
from keyring import get_credential as get_keyring_credential


# Triggers the keyring popup if the keyring is not unlocked already.
# Locks the thread until the popup is closed.
#
# The credentials requested are arbitrary, they are not of interest.
def trigger_keyring_unlock_popup():
    get_keyring_credential("service", "login")


# Create a thread to trigger the keyring unlock popup.
popup = Thread(target = trigger_keyring_unlock_popup)
popup.start()

# Wait a moment for the system to react
# Then check if the system is locked or not
time.sleep(1)
locked = popup.is_alive()

if (locked):
    print('The system is locked and a unlock popup has been triggered!')
