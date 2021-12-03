#!/usr/bin/env bash

if [ $# -ne 1 ]
then
    echo "Usage: ./fetch_input.sh \$day"
    exit 1
fi

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
SESSION=$(cat $SCRIPT_DIR/.session)
TEMP_FILE=$(mktemp)
RESULT_FILE="$SCRIPT_DIR/input/aoc_$1.txt"

echo "$SESSION"

HTTP_CODE=$(curl "https://adventofcode.com/2021/day/$1/input" -H "cookie: session=$SESSION" -o $TEMP_FILE -w '%{http_code}\n')

if [ "$HTTP_CODE" == "200" ]
then
    mv $TEMP_FILE $RESULT_FILE
    echo "Downladed input for day $1 to $RESULT_FILE"
else
    printf "Download failed. Http code: $HTTP_CODE.\nResponse:\n$(cat $TEMP_FILE)"
    rm $TEMP_FILE
fi
