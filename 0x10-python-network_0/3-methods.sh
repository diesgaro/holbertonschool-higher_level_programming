#!/bin/bash
# Bash script that get the value of Allow with curl and grep
curl -sI "$1" | grep Allow | cut -d' ' -f2-
