#!/bin/bash

if $OSTYPE = "linux-gnu"; then
    rm -r ~/Schreibtisch/RP
    rm -r ~/IdeaProjects/RP/src/__pycache__/
    mkdir ~/Schreibtisch/RP
    cp -r ~/IdeaProjects/RP/src/ ~/Schreibtisch/RP
fi