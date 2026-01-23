#!/bin/sh

curl -sIL $1 | grep -m1 "Location:" | cut -d' ' -f2 -
