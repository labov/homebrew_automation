#!/bin/bash

printy() {
  printf "\e[33;1m%s\n" "$1"
}
printg() {
  printf "\e[32m$1\e[m\n"
}
printr() {
  echo "\033[1;31m$1\033[0m"
}

printy "===  Mac setting start  =========================== \n"
printg "====  Install hoembrew  =========================== \n"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
export PATH=$PATH:/opt/homebrew/bin/
printy $PATH

printg "===  Run mac_setting.py  ========================== \n"
/usr/bin/python3 $DIR/mac-setting.py