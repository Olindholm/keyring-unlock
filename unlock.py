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
#
# If you use this script as intended, at bootup of system.
# Sometimes it will be run before the desktop enviroment
# has properly started, thus making it fail. Add a reasonable
# delay to overcome this problem. Emperical testing can be used.
password = ""
boottime = 0 # Seconds

# END OF CONFIGURATIONS! WARNING! DO NOT EDIT BELOW THIS LINE!

# Small delay for the desktop enviroment
# to have proper time to launch.
time.sleep(boottime)


# Triggers the keyring popup if the keyring is not unlocked already.
# Locks the thread until the popup is closed.
#
# The credentials requested are arbitrary, they are not of interest.
def trigger_keyring_unlock_popup():
    try:
        get_keyring_credential("service", "login")
    except:
        print("Keyring unlock popup closed! (cancelled)")


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
