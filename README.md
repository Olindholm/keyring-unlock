# Keyring Unlock
A small script to automatically unlock the keyring (seahorse) in Ubuntu.

---
<!---
## Table of contents
* [General info](#general-info)
* [Setup / Installation](#setup-/-installation)
* [Contact](#contact)

---
-->

## General Info
This project was developed for Ubuntu (19.10) but will very likely work with other Ubuntu versions as well as other distros too. I developed this project because I boot with auto login, which refuses to unlock your keyring despite my best efforts and google research. Many suggest, to put no password on your keyring, or to simply delete/remove keyrings alltogether. None of which worked for me (seems it might've worked for older versions of Ubuntu).

So, this script was developed, as set to run automatically after the system has booted, and saves the annoying prompt of entering your keyring password once you launch applications as Goole Chrome or Steam.

| Warning! Your password will now be stored in plain text. That is any program can read this it and your system is thus very insecure. Make sure you take other security measures to insure the safety of your system.  |
| --- |

---

## Dependencies
* [Python 3](https://www.python.org/download/releases/3.0/)
* [keyring](https://pypi.org/project/keyring/)
* [xdotool](https://github.com/jordansissel/xdotool)
* [Git](https://git-scm.com/) (optional but recommended)

Note this was developed for Ubuntu (version >= 19.10) but will very likely work with other Ubuntu versions as well as other distros too. Please do leave an comment/issue on your experience.

---

## Setup / Installation
| Note: This setup/installation guide is for ubuntu (and debian based distros) mainly. |
| --- |

First install the dependencies starting with [Python 3](https://www.python.org/download/releases/3.0/) (which you probably already), then we'll install pip3 to easily install [keyring](https://pypi.org/project/keyring/). Finally we also install [xdotool](https://github.com/jordansissel/xdotool) and [Git](https://git-scm.com/). [Git](https://git-scm.com/) isn't required for the script to work, but will be used during this installation process.

```bash
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
pip3 install keyring

sudo apt-get install xdotool
sudo apt-get install git
```

Let's move onto the script download, prefered way using git. Change directory to some prefered place, recommending your home directory.

```bash
cd ~
git clone https://github.com/Wiggyboy/keyring-unlock.git
```

Once git has downloaded the script, we'll configure it. In this example we'll use nano as our text editor, but you can use whatever you like.
```bash
cd keyring-unlock
nano unlock.py
```

| Warning! Your password will now be stored in plain text. That is any program can read this it and your system is thus very insecure. Make sure you take other security measures to insure the safety of your system.  |
| --- |

Now we edit the **password** and **boottime** at round around line 20. Set your password to the password used to unlock your keyring. The boottime can be left at 0 if you do not intend to run this script at boot. However if you do, set it to around 1-2 seconds if your system is fast, and 4-5 seconds if it's rather slow/old.

```python
password = ""
boottime = 0 # Seconds
```

Once that is configured, you can try if it works by running the command below. Make sure your keyring is locked, otherwise it won't actually do anything.
```bash
python3 unlock.py
```

So far if you've been running a debian based distro everything should've worked pretty easily, however that's about to change. You'll have to figure out exactly how to setup startup applications yourself if you're not running exactly Ubuntu (19.10) because the guide is getting very specific. However the process will by all likelyhood be very similiar and the **run script command should be almost if not exactly the same**.

Launch the **Startup Applications Preferences** via the **Dash**, click the **Add** button on the top right.
![test image size](/imgs/1.png)

Enter a name and comment to fit you. Then edit and enter the following command, i.e. change **\<user\>** to your linux username, or edit the whole path to where you placed the script in case you didn't go with the home directory.
```bash
python3 /home/<user/keyring-unlock/unlock.py
```
| Note: In my experience the path has to be exact not relative. <br> I.e. it cannot be `~/keyring-unlock/unlock.py` |
| --- |

![test image size](/imgs/2.png)

Finally click **Add** to finalize the entry and click **Close** because you're finished! Now it should work, you can reboot the system to try.

If it doesn't work, either by not seeming to do anything at all, or it leaving the password popup query, try increasing the **boottime** variable we configured previously.

---

## License
This project is licensed under the [MIT license](./LICENSE.md).
