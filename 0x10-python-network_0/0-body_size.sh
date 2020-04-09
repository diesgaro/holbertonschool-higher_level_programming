#!/bin/bash
# Bash script that get the value of Content-Length with curl and grep
curl -sI "$1" | grep Content-Length | cut -d' ' -f2
