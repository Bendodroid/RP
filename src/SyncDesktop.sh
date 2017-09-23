#!/bin/bash

if [[ "$OSTYPE" == "darwin"* ]]; then
    rm -f -r ~/Desktop/RP
    rm -f -r ~/IdeaProjects/RP/src/__pycache__/
    rm -f -r ~/IdeaProjects/RP/src/RP_Classes/__pycache__/
    mkdir ~/Desktop/RP/
    cp -r ~/IdeaProjects/RP/src/ ~/Desktop/RP/src/

elif [[ "$OSTYPE" == "linux-gnu" ]]; then
    rm -f -r ~/Schreibtisch/RP
    rm -f -r ~/IdeaProjects/RP/src/__pycache__/
    rm -f -r ~/IdeaProjects/RP/src/RP_Classes/__pycache__/
    mkdir ~/Schreibtisch/RP
    cp -r ~/IdeaProjects/RP/src/ ~/Schreibtisch/RP
fi
