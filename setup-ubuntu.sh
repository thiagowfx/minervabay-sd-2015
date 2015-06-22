#!/bin/sh
sudo apt-get install -y python-pip python-virtualenv
virtualenv python2
source python2/bin/activate
pip install -r requirements.txt
