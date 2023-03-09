#This package uses the functions from the webchecker package to create a function that plays different sounds as a bus is approaching its stop.
import os
from webchecker import *

r1 = ring1()
r2 = ring2()
r3 = ring3()
r4 = ring4()

def pysounds():
    if r1 == True:
        os.system("mpg123 then put in fullpathname for audio file1")
    elif r2 == True:
        os.system("mpg123 then put in fullpathname for audio file1")
    elif r3 == True:
        os.system("mpg123 then put in fullpathname for audio file1")
    elif r4 == True:
        os.system("mpg123 then put in fullpathname for audio file1")