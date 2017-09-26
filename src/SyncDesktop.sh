#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]; then
    rm -f -r ~/Desktop/RP
    rm -f -r ../src/__pycache__/
    rm -f -r ../src/RP_Classes/__pycache__/
    mkdir ~/Desktop/RP
    cp -r ../src ~/Desktop/RP

elif [[ "$OSTYPE" == "linux-gnu" ]]; then
    rm -f -r ~/Schreibtisch/RP
    rm -f -r ../src/__pycache__/
    rm -f -r ../src/RP_Classes/__pycache__/
    mkdir ~/Schreibtisch/RP
    cp -r ../src ~/Schreibtisch/RP
fi
