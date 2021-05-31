#!/bin/bash
rm file1.txt
for i in {0..999999}
do
    echo $RANDOM >> file1.txt
done
ECHO $SECONDS