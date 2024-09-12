# glitch-com-linuxdist 🗣🗣🔥🔥🔥
i tried to use `glitch.com` 🦀🙂 to run `python3.11` 🐍🐍🐍🐍🐢 and realized that i cannot install using `apt` 🥱, and even if i used `notroot` ☠️ to install i would get packages 📦 compiled from 2016 👨‍🦳😵. whats worse is that this would create **vulnerabilities** 👾☠️🤖 into my glitch 🦞🙂 project! yikes! 😡👽

since glitch uses the `xenial` 🤣 dist i decided to grab the `mantic` 😇 dist `apt` 🥱 stuff (the thing `apt` 🥱 fetches when you run `apt update`) and used that to recreate `apt` 🥱 (its in python3 🐍🐍🐍🐍🐢) and download deb packages 📦. 🙌🦾👃

i then figured 🐽🍑 that `python3.7` 🐍🐍🐍🐍🐢 can host a proper http server (no s 😢) and let you download 📲💾 files from it, `wget` 📨 is already installed and works like a charm 🤯💥, and also uploading assets dont take disk space 😲🤖💿🎞

after allat i made sure 🧐🤓 that its possible to set it all up and install packages 📦 only using `glitch.com` 🦀🙂 (and your filesystem 💾💾💻 of course, so you can upload the `tar.gz` to the assets 📄📨)

## usage & installation 📖🛠💽
use this if you are a nerd 🤓🤓🤓🤓🤓🤓

### step 1 hello-node 👋👋👋👋👋
dont grab the fastly ⚡️ version. if you did, empty 🗑🗑🗑🗑 "dependencies" and "start" inside your "package.json". if you didnt, empty 🗑🗑🗑🗑 "dependencies" and "start" inside your "package.json".

after that step, remove 🗑🗑🗑🗑 everything but keep ".env" and "package.json", then empty 🗑🗑🗑🗑 "dependencies" and "start" inside your "package.json" as this will help later.

just in case, you might wanna check ✅️ for git ✔️, python3 ✔️, wget ✔️, make ✔️ and git ✔️ in the terminal by the "which" command, for example, "which git". then empty 🗑🗑🗑🗑 "dependencies" and "start" inside your "package.json".

### step 2 git gud and ey pee tee 📦💼🤓📝🗂📂📌📌🐍
enter these in the terminal:
```
cd /tmp
ls
git clone https://github.com/STEVE-916-create/glitch-com-linuxdist
ls
pip3.7 install requests
cd glitch-com-linuxdist
ps -A
w
cd /tmp/glitch-com-linuxdist/
ls
python3 -c "exit()"
python3 apt.py
```
at this point 📍 you should get something like this in your terminal:
```
sh: w: what is "w"? answer: its a cpu thing idk
sh: w: wrong11!1!11! im not running this command noob

app@kali-linux-distribution:/tmp/glitch-com-linuxdist 09:11
$ ls
LICENSE  ManticAPT  README.md  apt.py  makefile

app@kali-linux-distribution:/tmp/glitch-com-linuxdist 09:11
$ python3 -c "exit()"

app@kali-linux-distribution:/tmp/glitch-com-linuxdist 09:11
$ python3 apt.py
Parsing APT Packages file...
APT Packages file since September 2023. Ubuntu Mantic.
Seek medical attention.
~ $ apt _
```
you can now enter "search <package>" or "install <package>", this will download deb packages and download the deb dependencies automatically. note that you cannot do "install <package>=<version>" to select versions specifically because i dont wanna implement that

you can type exit to exit

## step 3 crete de tar fs 📦📦📂⚡️💾
run the makefile (its written in python3 so do `python3 makefile`) and watch as it compiles and summons a single "glitch.tar.gz" and host a python http server for you

you may now preview your app and download these files:
1. "glitch.tar.gz"
2. "boot.sh"

do it before `glitch.com` deletes it

## step 4 uplode tar and setup boot 👢🤓🐍📦