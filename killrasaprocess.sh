#!/bin/bash
#this script is to automate kill process
declare -a arr=$(pgrep rasa)
echo "$arr"
IFS=$'\n'
for i in $arr
do
      kill $i
done
conda init bash
chmod a+rwx models
rasa train
BUILD_ID=dontKillMe nohup rasa run --enable-api --cors "*" --debug &
BUILD_ID=dontKillMe nohup rasa run actions --debug &
