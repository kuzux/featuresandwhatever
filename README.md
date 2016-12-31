Reads a bunch of sensor data from some csv files, calculates a few features and spits them back out as new csv files.

Input file format: {Bag/Hand/Pocket}/{acc/gyro}N.csv

Output format: userN.csv

How to run: you need a python interpreter, and have pandas and numpy installed. Then run `python process.py` to process the data. For 15 users * 6 files each (each csv = around 50K lines) the whole process took about a minute. Tested on OSX Yosemite with python 2.7.10
