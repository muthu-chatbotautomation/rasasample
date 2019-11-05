#!/bin/bash
#this script is to automate kill process
declare arr=$(pgrep rasa)
echo "$arr"
IFS=$'\n'
for i in $arr
do
      kill $i
done

