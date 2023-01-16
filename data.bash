#!/bin/bash

for hour in {00..23}
do
	filename=$(aws s3 ls --no-sign-request s3://noaa-goes16/ABI-L2-DMWF/${2}/${1}/${hour}/ | tr -s ' ' | cut -d' ' -f4 | grep C02)
	echo ${filename}
	wget https://noaa-goes16.s3.amazonaws.com/ABI-L2-DMWF/$2/$1/${hour}/${filename} -P data_$1_$2
done

python3 analisis.py $1 $2
