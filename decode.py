#!/usr/bin/python3

import re
import sys

polynom = ""
while(not re.match("^(0|1)+$", polynom)):
	polynom = input("Enter coefficients of the polynom (binary): ")[::-1]

known_s = ""
while(not re.match("^(0|1)+$", known_s)):
	known_s = input("Enter " + str(len(polynom)) + " known initial values (binary): ")

length = int(input("How many values should be calculated? "))

if(len(known_s) < len(polynom)):
	print("Error: " + str(len(known_s)) + " < " + str(len(polynom)))
	sys.exit()

s = [0]*length											
dec = ""

for i in range(len(known_s)):
	s[i] = int(known_s[i])

for i in range(len(known_s), length):
	s[i] = s[i-len(polynom)]*int(polynom[0])

	for j in range(1, len(polynom)):
		s[i] ^= s[i-len(polynom)+j]*int(polynom[j])

print("Stream: " + str(s))
