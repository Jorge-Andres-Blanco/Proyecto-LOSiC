#!/bin/bash
rm -r data_$1_$2
mkdir data_$1_$2
cd data_$1_$2
for hour in {13..23}
do
	filename=$(aws s3 ls --no-sign-request s3://noaa-goes16/ABI-L2-DMWF/${2}/${1}/${hour}/ | tr -s ' ' | cut -d' ' -f4 | grep C02)
	wget https://noaa-goes16.s3.amazonaws.com/ABI-L2-DMWF/$2/$1/${hour}/${filename}
	python3 ../analisis.py ${filename}
	rm ${filename}
done
cd ..