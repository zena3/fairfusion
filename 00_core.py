#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# default_exp core


# # Temperature
# 
# > This example displays the ambient/room and hot junction temperatures at 1 second intervals. 
# Turn on the Mu editor's plotter option to view the temperatures in a real-time graph.
# 
# ## if temp >22 graden send notification
# pin nr 19, 22 24

# In[1]:


#hide
from nbdev.showdoc import *


# In[2]:


#install adafruit in your virtual environment.
#pip3 install adafruit-io
#see requirements


# In[6]:


import board
import busio
import time
import csv
from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_mcp9600 import MCP9600


# In[7]:


i2c = busio.I2C(board.SCL, board.SDA, frequency=200000)

try:
    device = MCP9600(i2c)
    print("version:", device.version)
    while True:
        print((
            device.ambient_temperature,
            device.temperature
        ))
        #set the observation frequency - 1 means every second
        time.sleep(1)
except ValueError:
    print("MCP9600 sensor not detected")

#register data in csv file
csv_file = open('temp.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['time', 'temperature'])
csv_file.close()

