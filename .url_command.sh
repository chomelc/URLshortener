#!/bin/bash

function surl {
    if [ "$#" -ne 1 ]; 
    then
        tput setaf 1; echo "Command failed. Please type the URL to shorten."
        return 1
    fi
    python3 ~/Documents/URLshortener/URLshortener.py $1
}