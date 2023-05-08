#!/bin/sh

git clone https://github.com/mininet/mininet
mininet/util/install.sh -a
sudo mn --switch ovsbr --test pingall