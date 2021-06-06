#!/bin/bash
SECONDS=0
while read -r number
do
  let "number *= 2"
  echo $number >> newfile1.txt
done < ../shell/file1.txt
duration=$SECONDS
echo $duration