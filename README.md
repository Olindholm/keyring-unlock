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

Do note the use of this script makes your system rather insecure and vulnerable. So make sure to take other security measures.

---

## Dependencies
* [Python 3](https://www.python.org/download/releases/3.0/)
* [keyring](https://pypi.org/project/keyring/)
* [xdotool](https://github.com/jordansissel/xdotool)

Note this was developed for Ubuntu (version >= 19.10) but will very likely work with other Ubuntu versions as well as other distros too. Please do leave an comment/issue on your experience.

---

## Setup / Installation
TODO: Describe how to install / setup your local environement / add link to demo version.

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright &copy; 2019 Wiggy boy \<Lindholm\>\
  (formally known as Osvald Lindholm)