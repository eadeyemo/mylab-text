#!/usr/bin/python
import subprocess
##Inserting host IP using raw_input
host = raw_input("Enter a host IP address to check firewall status: ")
cs = subprocess.Popen(['csf', '-g', host], stdout=subprocess.PIPE)
csf = cs.communicate()
print csf 
