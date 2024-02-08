#!/usr/bin/env bash
#
# This script assumes it is being called from the root of the repo

DB=$(pwd)/checker.db

if [ ! -f "$DB" ]; then
    echo "Creating $DB"
    sqlite3 "$DB" "VACUUM;"
fi

docker build -t checker:latest . && docker run -v "$DB:/checker.db" checker:latest

