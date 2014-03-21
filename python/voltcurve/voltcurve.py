#!/usr/bin/python

import sys
import serial

if len(sys.argv) != 2:
  print "takes either read(r) or write(w) as an argument"
  sys.exit(0)

if sys.argv[1]  != '-r' and sys.argv[1] != '-w':
  print "take either r or w"
  sys.exit(0)

if sys.argv[1] == '-r':
  ser = serial.Serial('/dev/ttyACM0', 9600) # Start Reading Serial data
  volts = 1 #anything just not 0
  f = open('info.txt', 'w')
  count = 0
  try:
    while volts == 1:# Read until volts are 0 except at beginning
      sval = ser.readline()
      print sval
      batt = sval[0:4] + "\n"
      f.write(batt)
      #volts = int(float(sval.rstrip("\r\n"))) #round to in and then will quit when < 1 volt    
      temp = sval[4:]
      temp.rstrip("\r\n")
      volts = int(temp)
      if count == 100: 
        f.close()
        f=open('info.txt', 'a')
        print "Clearing file memory"
	count = 0
      else:
        count = count + 1
  except KeyboardInterrupt: #To close up the file on exit if ending befoe 0 volts
    print "Exiting"
    f.close()
    pass

if sys.argv[1] == '-w':
  print "Write here"
  #f = open('info.txt', 'r')
  #farr = (line.rstrip("\r\n") for line in open("info.txt")) 
  #f.close()
  #print len(farr)
  with open('info.txt', 'r') as f:
    farr = [float(line.rstrip("\r\n")) for line in f]
  time = len(farr)
  threeqrt = farr[int(time*.25)]
  half = farr[(time/2)]	
  oneqrt = farr[int(time*.75)]
  ten = farr[int(time * .9)]
  print "75% = " + str(threeqrt)
  print "50% = " + str(half)
  print "25% = " + str(oneqrt)
  print "10% = " + str(ten)
  print "ran " + str(time) + " seconds"
sys.exit(0)
