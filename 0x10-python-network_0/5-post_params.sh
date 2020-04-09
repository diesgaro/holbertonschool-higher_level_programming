#!/bin/bash
# Bash script that sends variables with post method
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
