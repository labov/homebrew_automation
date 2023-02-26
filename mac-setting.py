import os
import time
from pathlib import Path

## run sh sh_mac-setting.sh
os.system("export PATH=$PATH:/opt/homebrew/bin/")
os.system("echo $PATH")

## check brew path in $HOME/.zprofile
brew_path = "export PATH=$PATH:/opt/homebrew/bin/"
home = str(Path.home())
f = open(f"{home}/.zprofile", "a+")
lines = f.readlines()
flags = []
for i in lines:
    flags.append(i == brew_path)
f.close

## add brew path
f = open(f"{home}/.zprofile", "a+")
if True in flags:
    print("brew path exist")
else:
    f.write("\n")
    f.write(brew_path)
f.close

## install app names
apps = [
    "aldente",
    "raycast",
    "karabiner-elements",
    "rectangle",
    "cheatsheet",
    "monitorcontrol",
    "popclip",
    "numi",
    "google-chrome",
    "sourcetree",
    "visual-studio-code",
    "anydesk",
    "slack",
    "obsidian",
    "dropbox",
    "cocoapods",
    "easyfind",
    "onlyoffice",
    "keycastr",
    "hiddenbar",
    "maccy",
    "shottr",
    "alt-tab",
    "dropzone",
    "appcleaner",
    "the-unarchiver",
    "skim",
    "imageoptim",
    "pdf-squeezer",
    "icloud-control",
    "stats",
    ## optional
    # "tableau-public",
    # 'mongodb-community',
    # 'mongodb-compass',
    # 'blender',
    # "flutter",
    # "android-studio",
    ## need password
    # 'chrome-remote-desktop-host',
]
manual = [
    "synergy",
]
appstore = ["xocde", "QR Capture"]
brew_cmd = [
    "install",
    "upgrade",
    "uninstall",
]

## option select string maker
option_select = ""
for i in brew_cmd:
    option_select = option_select + f"\n {brew_cmd.index(i)}:{i} "

## option number check loop
while True:
    print(f"Select options : {option_select}")
    print(f"Select from 0~{len(brew_cmd)-1}")
    option = int(input())

    ## brew command
    if option >= 0 and option <= len(brew_cmd):
        for app in apps:
            os.system(f"brew {brew_cmd[option]} {app}")
        break
    else:
        time.sleep(2)
