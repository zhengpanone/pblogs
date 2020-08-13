#!/bin/sh

for (i=1; i< 1000; i++)
do
    d = `date '+ %Y-%m-%d %H:%M:%S'`
    echo "$d print ${i}"
    sleep 2s

done