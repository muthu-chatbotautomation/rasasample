#!/bin/bash
#this script is to automate kill process
declare -a arr=$(pgrep rasa)
echo "$arr"
IFS=$'\n'
for i in $arr
do
      kill $i
done
sudo chmod ugo+rwx killrasaprocess.sh
