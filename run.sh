#!/usr/bin/env bash
#
# This script assumes it is being called from the root of the repo

DB=$(pwd)/checker.db

if [ -z "$DB" ]; then
    touch "$DB"

docker build -t checker:latest . && docker run -it -v "$DB:/checker.db" checker:latest

