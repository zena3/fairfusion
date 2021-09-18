# FairFusion - Measuring Temperature
This repo contains code for running the Adafruit DHT22 temperature and humidity sensor with a RaspberryPi. You can register the all sensory measurements in a csv file with a date and time stamp. In addition, you can adjust the following settings: measurement interval (time) and storage location.

## Setting up your environment
Equipment
- Temperature sensor: Adafruit DHT22
- CPU: Rapsberry Pi

Make sure you set the correct pin position [insert picture]. By default, pin position number 4 is selected but this can be adjusted in temp_reg_p.py.

### Preparing your Raspberry Pi
In the terminal, run the following commands first:
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install build-essential python-dev 
- sudo pip3 install Adafruit-DHT

## Measuring Temperature
After installing the above successfully, it's time to run your python file and start your measurements. Run:
```
python3 temp_reg_p.py
```
A new csv file is created in your designated folder and you'll see print statements in your terminal. Sit back and relax. Nah kidding, you gotta continue with your research!