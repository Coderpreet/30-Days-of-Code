#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

tip_percent = meal_cost * (tip_percent / 100)  
tax_percent = meal_cost * (tax_percent / 100) 
totalcost = float( meal_cost + tip_percent + tax_percent)  
print(round(totalcost))

#this is for python3
