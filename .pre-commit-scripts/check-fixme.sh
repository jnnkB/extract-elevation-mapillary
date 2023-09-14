#!/bin/sh

matches=$(git diff --cached | grep -E '\+.*?FIX''ME')

if [ "$matches" != "" ]
then
        echo "'FIX""ME' tag is detected."
        echo "Please fix it before committing."
        echo "  ${matches}"
        exit 1
fi
