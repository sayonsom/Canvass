#!/bin/bash
# My first script


echo "ADS HAS BEEN ACTIVATED"
echo "------------------------"
SECONDS=0
#bg
sudo python respondtolivecapture.py
echo "ADS was turned on for --> $SECONDS seconds"
